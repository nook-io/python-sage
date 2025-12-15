from __future__ import absolute_import
import six
from sage.api_client import ApiClient
from sage.exceptions import ApiTypeError, ApiValueError


class BusinessSettingsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_business_settings(self, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_business_settings_with_http_info(**kwargs)

    def get_business_settings_with_http_info(self, **kwargs):
        local_var_params = locals()
        all_params = []
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_business_id",
            ]
        )
        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_business_settings" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        if (
            "_business_id" in local_var_params
            and local_var_params["_business_id"] is not None
        ):
            header_params["X-Business"] = local_var_params["_business_id"]
        auth_settings = ["OAuth2"]
        return self.api_client.call_api(
            "/business_settings",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BusinessSettings",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_business_settings(self, business_settings, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.put_business_settings_with_http_info(business_settings, **kwargs)

    def put_business_settings_with_http_info(self, business_settings, **kwargs):
        local_var_params = locals()
        all_params = ["business_settings"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_business_id",
            ]
        )
        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_business_settings" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "business_settings" not in local_var_params
            or local_var_params["business_settings"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `business_settings` when calling `put_business_settings`"
            )
        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None
        if "business_settings" in local_var_params:
            body_params = local_var_params["business_settings"]
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )
        if (
            "_business_id" in local_var_params
            and local_var_params["_business_id"] is not None
        ):
            header_params["X-Business"] = local_var_params["_business_id"]
        header_params["Content-Type"] = self.api_client.select_header_content_type(
            ["application/json"]
        )
        auth_settings = ["OAuth2"]
        return self.api_client.call_api(
            "/business_settings",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BusinessSettings",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
