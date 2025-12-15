from __future__ import absolute_import
import six
from sage.api_client import ApiClient
from sage.exceptions import ApiTypeError, ApiValueError


class BusinessExchangeRatesApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_business_exchange_rates_key(self, key, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.delete_business_exchange_rates_key_with_http_info(key, **kwargs)

    def delete_business_exchange_rates_key_with_http_info(self, key, **kwargs):
        local_var_params = locals()
        all_params = ["key"]
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
                    " to method delete_business_exchange_rates_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `delete_business_exchange_rates_key`"
            )
        collection_formats = {}
        path_params = {}
        if "key" in local_var_params:
            path_params["key"] = local_var_params["key"]
        query_params = []
        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None
        auth_settings = ["OAuth2"]
        return self.api_client.call_api(
            "/business_exchange_rates/{key}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_business_exchange_rates(self, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_business_exchange_rates_with_http_info(**kwargs)

    def get_business_exchange_rates_with_http_info(self, **kwargs):
        local_var_params = locals()
        all_params = ["items_per_page", "page", "attributes"]
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
                    " to method get_business_exchange_rates" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] > 200
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_business_exchange_rates`, must be a value less than or equal to `200`"
            )
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] < 1
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_business_exchange_rates`, must be a value greater than or equal to `1`"
            )
        collection_formats = {}
        path_params = {}
        query_params = []
        if (
            "items_per_page" in local_var_params
            and local_var_params["items_per_page"] is not None
        ):
            query_params.append(("items_per_page", local_var_params["items_per_page"]))
        if "page" in local_var_params and local_var_params["page"] is not None:
            query_params.append(("page", local_var_params["page"]))
        if (
            "attributes" in local_var_params
            and local_var_params["attributes"] is not None
        ):
            query_params.append(("attributes", local_var_params["attributes"]))
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
            "/business_exchange_rates",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[BusinessExchangeRate]",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_business_exchange_rates_key(self, key, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_business_exchange_rates_key_with_http_info(key, **kwargs)

    def get_business_exchange_rates_key_with_http_info(self, key, **kwargs):
        local_var_params = locals()
        all_params = ["key", "attributes"]
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
                    " to method get_business_exchange_rates_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `get_business_exchange_rates_key`"
            )
        collection_formats = {}
        path_params = {}
        if "key" in local_var_params:
            path_params["key"] = local_var_params["key"]
        query_params = []
        if (
            "attributes" in local_var_params
            and local_var_params["attributes"] is not None
        ):
            query_params.append(("attributes", local_var_params["attributes"]))
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
            "/business_exchange_rates/{key}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BusinessExchangeRate",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_business_exchange_rates(self, business_exchange_rates, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.post_business_exchange_rates_with_http_info(
            business_exchange_rates, **kwargs
        )

    def post_business_exchange_rates_with_http_info(
        self, business_exchange_rates, **kwargs
    ):
        local_var_params = locals()
        all_params = ["business_exchange_rates"]
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
                    " to method post_business_exchange_rates" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "business_exchange_rates" not in local_var_params
            or local_var_params["business_exchange_rates"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `business_exchange_rates` when calling `post_business_exchange_rates`"
            )
        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None
        if "business_exchange_rates" in local_var_params:
            body_params = local_var_params["business_exchange_rates"]
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
            "/business_exchange_rates",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BusinessExchangeRate",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_business_exchange_rates_key(self, key, business_exchange_rates, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.put_business_exchange_rates_key_with_http_info(
            key, business_exchange_rates, **kwargs
        )

    def put_business_exchange_rates_key_with_http_info(
        self, key, business_exchange_rates, **kwargs
    ):
        local_var_params = locals()
        all_params = ["key", "business_exchange_rates"]
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
                    " to method put_business_exchange_rates_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `put_business_exchange_rates_key`"
            )
        if self.api_client.client_side_validation and (
            "business_exchange_rates" not in local_var_params
            or local_var_params["business_exchange_rates"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `business_exchange_rates` when calling `put_business_exchange_rates_key`"
            )
        collection_formats = {}
        path_params = {}
        if "key" in local_var_params:
            path_params["key"] = local_var_params["key"]
        query_params = []
        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None
        if "business_exchange_rates" in local_var_params:
            body_params = local_var_params["business_exchange_rates"]
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
            "/business_exchange_rates/{key}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BusinessExchangeRate",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
