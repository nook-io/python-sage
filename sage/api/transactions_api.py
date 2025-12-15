from __future__ import absolute_import
import six
from sage.api_client import ApiClient
from sage.exceptions import ApiTypeError, ApiValueError


class TransactionsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_transactions(self, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_transactions_with_http_info(**kwargs)

    def get_transactions_with_http_info(self, **kwargs):
        local_var_params = locals()
        all_params = [
            "updated_or_created_since",
            "from_date",
            "to_date",
            "updated_from_date",
            "updated_to_date",
            "has_attachments",
            "items_per_page",
            "page",
            "attributes",
            "transaction_type_id",
        ]
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
                    " to method get_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] > 200
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_transactions`, must be a value less than or equal to `200`"
            )
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] < 1
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_transactions`, must be a value greater than or equal to `1`"
            )
        collection_formats = {}
        path_params = {}
        query_params = []
        if (
            "updated_or_created_since" in local_var_params
            and local_var_params["updated_or_created_since"] is not None
        ):
            query_params.append(
                (
                    "updated_or_created_since",
                    local_var_params["updated_or_created_since"],
                )
            )
        if (
            "from_date" in local_var_params
            and local_var_params["from_date"] is not None
        ):
            query_params.append(("from_date", local_var_params["from_date"]))
        if "to_date" in local_var_params and local_var_params["to_date"] is not None:
            query_params.append(("to_date", local_var_params["to_date"]))
        if (
            "updated_from_date" in local_var_params
            and local_var_params["updated_from_date"] is not None
        ):
            query_params.append(
                ("updated_from_date", local_var_params["updated_from_date"])
            )
        if (
            "updated_to_date" in local_var_params
            and local_var_params["updated_to_date"] is not None
        ):
            query_params.append(
                ("updated_to_date", local_var_params["updated_to_date"])
            )
        if (
            "has_attachments" in local_var_params
            and local_var_params["has_attachments"] is not None
        ):
            query_params.append(
                ("has_attachments", local_var_params["has_attachments"])
            )
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
        if (
            "transaction_type_id" in local_var_params
            and local_var_params["transaction_type_id"] is not None
        ):
            query_params.append(
                ("transaction_type_id", local_var_params["transaction_type_id"])
            )
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
            "/transactions",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[Transaction]",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_transactions_key(self, key, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_transactions_key_with_http_info(key, **kwargs)

    def get_transactions_key_with_http_info(self, key, **kwargs):
        local_var_params = locals()
        all_params = ["key", "expand_origin", "attributes"]
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
                    " to method get_transactions_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `get_transactions_key`"
            )
        collection_formats = {}
        path_params = {}
        if "key" in local_var_params:
            path_params["key"] = local_var_params["key"]
        query_params = []
        if (
            "expand_origin" in local_var_params
            and local_var_params["expand_origin"] is not None
        ):
            query_params.append(("expand_origin", local_var_params["expand_origin"]))
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
            "/transactions/{key}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Transaction",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
