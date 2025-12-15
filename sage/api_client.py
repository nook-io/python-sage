from __future__ import absolute_import
import atexit
import datetime
import json
import mimetypes
import os
import re
import tempfile
from multiprocessing.pool import ThreadPool
import six
from dateutil.parser import parse
from six.moves.urllib.parse import quote
import sage.models
from sage import rest
from sage.configuration import Configuration
from sage.exceptions import (
    ApiException,
    ApiValueError,
    OAuth2TokenGetterError,
    OAuth2TokenSaverError,
)


class ApiClient(object):
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        "int": int,
        "long": int if six.PY3 else long,
        "float": float,
        "str": str,
        "bool": bool,
        "date": datetime.date,
        "datetime": datetime.datetime,
        "object": object,
    }
    _pool = None

    def __init__(
        self,
        configuration=None,
        header_name=None,
        header_value=None,
        cookie=None,
        pool_threads=1,
        oauth2_token_saver=None,
        oauth2_token_getter=None,
    ):
        if configuration is None:
            configuration = Configuration.get_default_copy()
        self.configuration = configuration
        self.pool_threads = pool_threads
        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        self.user_agent = "OpenAPI-Generator/1.0.0/python"
        self.client_side_validation = configuration.client_side_validation
        self._oauth2_token_saver = oauth2_token_saver
        self._oauth2_token_getter = oauth2_token_getter

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None
            if hasattr(atexit, "unregister"):
                atexit.unregister(self.close)

    @property
    def pool(self):
        if self._pool is None:
            atexit.register(self.close)
            self._pool = ThreadPool(self.pool_threads)
        return self._pool

    @property
    def user_agent(self):
        return self.default_headers["User-Agent"]

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers["User-Agent"] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_type=None,
        auth_settings=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
        _host=None,
    ):
        config = self.configuration
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params["Cookie"] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params, collection_formats)
            )
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                resource_path = resource_path.replace(
                    "{%s}" % k, quote(str(v), safe=config.safe_chars_for_path_param)
                )
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params, collection_formats)
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params, collection_formats)
            post_params.extend(self.files_parameters(files))
        self.update_params_for_auth(header_params, query_params, auth_settings)
        if body:
            body = self.sanitize_for_serialization(body)
        if "oauth" in resource_path:
            url = resource_path
        elif _host is None:
            url = self.configuration.host + resource_path
        else:
            url = _host + resource_path
        try:
            response_data = self.request(
                method,
                url,
                query_params=query_params,
                headers=header_params,
                post_params=post_params,
                body=body,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
            )
        except ApiException as e:
            e.body = e.body.decode("utf-8") if six.PY3 else e.body
            raise e
        content_type = response_data.getheader("content-type")
        self.last_response = response_data
        return_data = response_data
        if not _preload_content:
            return return_data
        if six.PY3 and response_type not in ["file", "bytes"]:
            match = None
            if content_type is not None:
                match = re.search(r"charset=([a-zA-Z\-\d]+)[\s\;]?", content_type)
            encoding = match.group(1) if match else "utf-8"
            response_data.data = response_data.data.decode(encoding)
        if response_type:
            return_data = self.deserialize(response_data, response_type)
        else:
            return_data = None
        if _return_http_data_only:
            return return_data
        else:
            return (return_data, response_data.status, response_data.getheaders())

    def sanitize_for_serialization(self, obj):
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        if isinstance(obj, dict):
            obj_dict = obj
        else:
            obj_dict = {
                obj.attribute_map[attr]: getattr(obj, attr)
                for attr, _ in six.iteritems(obj.openapi_types)
                if getattr(obj, attr) is not None
            }
        return {
            key: self.sanitize_for_serialization(val)
            for key, val in six.iteritems(obj_dict)
        }

    def deserialize(self, response, response_type):
        if response_type == "file":
            return self.__deserialize_file(response)
        try:
            data = json.loads(response.data)
        except ValueError:
            data = response.data
        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        if data is None:
            return None
        data_type = type(data)
        if data_type == str and klass.startswith("dict(") and "$error" in data:
            raise ApiException(status=400)
        if type(klass) == str:
            if klass.startswith("list["):
                sub_kls = re.match(r"list\[(.*)\]", klass).group(1)
                if "$items" in data:
                    return [
                        self.__deserialize(sub_data, sub_kls)
                        for sub_data in data["$items"]
                    ]
                else:
                    return [self.__deserialize(sub_data, sub_kls) for sub_data in data]
            if klass.startswith("dict("):
                sub_kls = re.match(r"dict\(([^,]*), (.*)\)", klass).group(2)
                return {
                    k: self.__deserialize(v, sub_kls) for k, v in six.iteritems(data)
                }
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(sage.models, klass)
        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datetime(data)
        else:
            return self.__deserialize_model(data, klass)

    def call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_type=None,
        auth_settings=None,
        async_req=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
        _host=None,
    ):
        if not async_req:
            return self.__call_api(
                resource_path,
                method,
                path_params,
                query_params,
                header_params,
                body,
                post_params,
                files,
                response_type,
                auth_settings,
                _return_http_data_only,
                collection_formats,
                _preload_content,
                _request_timeout,
                _host,
            )
        return self.pool.apply_async(
            self.__call_api,
            (
                resource_path,
                method,
                path_params,
                query_params,
                header_params,
                body,
                post_params,
                files,
                response_type,
                auth_settings,
                _return_http_data_only,
                collection_formats,
                _preload_content,
                _request_timeout,
                _host,
            ),
        )

    def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        if method == "GET":
            return self.rest_client.GET(
                url,
                query_params=query_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                headers=headers,
            )
        elif method == "HEAD":
            return self.rest_client.HEAD(
                url,
                query_params=query_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                headers=headers,
            )
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(
                url,
                query_params=query_params,
                headers=headers,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
            )
        elif method == "POST":
            return self.rest_client.POST(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "PUT":
            return self.rest_client.PUT(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "PATCH":
            return self.rest_client.PATCH(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "DELETE":
            return self.rest_client.DELETE(
                url,
                query_params=query_params,
                headers=headers,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        else:
            raise ApiValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in six.iteritems(params) if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == "multi":
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == "ssv":
                        delimiter = " "
                    elif collection_format == "tsv":
                        delimiter = "\t"
                    elif collection_format == "pipes":
                        delimiter = "|"
                    else:
                        delimiter = ","
                    new_params.append((k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def files_parameters(self, files=None):
        params = []
        if files:
            for k, v in six.iteritems(files):
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, "rb") as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = (
                            mimetypes.guess_type(filename)[0]
                            or "application/octet-stream"
                        )
                        params.append(tuple([k, tuple([filename, filedata, mimetype])]))
        return params

    def select_header_accept(self, accepts):
        if not accepts:
            return
        accepts = [x.lower() for x in accepts]
        if "application/json" in accepts:
            return "application/json"
        else:
            return ", ".join(accepts)

    def select_header_content_type(self, content_types):
        if not content_types:
            return "application/json"
        content_types = [x.lower() for x in content_types]
        if "application/json" in content_types or "*/*" in content_types:
            return "application/json"
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings):
        if not auth_settings:
            return
        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings(auth)
            if callable(auth_setting):
                auth_setting = auth_setting(api_client=self)
            if auth_setting:
                if auth_setting["in"] == "cookie":
                    headers["Cookie"] = auth_setting["value"]
                elif auth_setting["in"] == "header":
                    headers[auth_setting["key"]] = auth_setting["value"]
                elif auth_setting["in"] == "query":
                    querys.append((auth_setting["key"], auth_setting["value"]))
                else:
                    raise ApiValueError(
                        "Authentication token must be in `query` or `header`"
                    )

    def __deserialize_file(self, response):
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)
        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.search(
                r'filename=[\'"]?([^\'"\s]+)[\'"]?', content_disposition
            ).group(1)
            path = os.path.join(os.path.dirname(path), filename)
        with open(path, "wb") as f:
            f.write(response.data)
        return path

    def __deserialize_primitive(self, data, klass):
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        return value

    def __deserialize_date(self, string):
        if string == "":
            return None
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0, reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datetime(self, string):
        if string == "":
            return None
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=("Failed to parse `{0}` as datetime object".format(string)),
            )

    def __deserialize_model(self, data, klass):
        has_discriminator = False
        if (
            hasattr(klass, "get_real_child_model")
            and klass.discriminator_value_class_map
        ):
            has_discriminator = True
        if not klass.openapi_types and has_discriminator is False:
            return data
        kwargs = {}
        if (
            data is not None
            and klass.openapi_types is not None
            and isinstance(data, (list, dict))
        ):
            for attr, attr_type in six.iteritems(klass.openapi_types):
                if klass.attribute_map[attr] in data:
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)
        instance = klass(**kwargs)
        if has_discriminator:
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance

    def get_oauth2_token(self):
        if not self._oauth2_token_getter:
            raise OAuth2TokenGetterError(
                "Invalid oauth2_token_getter={!r} function".format(
                    self._oauth2_token_getter
                )
            )
        return self._oauth2_token_getter()

    def set_oauth2_token(self, token):
        if not self._oauth2_token_saver:
            raise OAuth2TokenSaverError(
                "Invalid oauth2_token_saver={!r} function".format(
                    self._oauth2_token_saver
                )
            )
        self._oauth2_token_saver(token)

    def refresh_oauth2_token(self):
        oauth2_token = self.configuration.oauth2_token
        oauth2_token.update_token(**self.get_oauth2_token())
        if oauth2_token.refresh_access_token(self):
            return self.get_oauth2_token()

    def revoke_oauth2_token(self):
        oauth2_token = self.configuration.oauth2_token
        oauth2_token.update_token(
            **{
                "access_token": None,
                "expires_in": None,
                "token_type": "Bearer",
                "refresh_token": None,
                "refresh_token_expires_in": None,
                "scope": None,
                "requested_by_id": None,
            }
        )
        if oauth2_token.revoke_access_token(self):
            return self.get_oauth2_token()

    def get_client_credentials_token(self, app_store_billing=False):
        oauth2_token = self.configuration.oauth2_token
        if oauth2_token.get_client_credentials_access_token(self, app_store_billing):
            return self.get_oauth2_token()

    def oauth2_token_getter(self, token_getter):
        self._oauth2_token_getter = token_getter
        return token_getter

    def oauth2_token_saver(self, token_saver):
        self._oauth2_token_saver = token_saver
        return token_saver
