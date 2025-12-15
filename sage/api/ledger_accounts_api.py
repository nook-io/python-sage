from __future__ import absolute_import
import six
from sage.api_client import ApiClient
from sage.exceptions import ApiTypeError, ApiValueError


class LedgerAccountsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_ledger_accounts(self, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_ledger_accounts_with_http_info(**kwargs)

    def get_ledger_accounts_with_http_info(self, **kwargs):
        local_var_params = locals()
        all_params = [
            "updated_or_created_since",
            "visible_in",
            "not_visible_in",
            "show_included_in_chart",
            "show_control_accounts",
            "ledger_account_classification_id",
            "show_balance_details",
            "exclude_deleted_entries",
            "from_date",
            "to_date",
            "search",
            "sort_order_from_user_setting",
            "items_per_page",
            "page",
            "attributes",
            "ledger_account_type_id",
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
                    " to method get_ledger_accounts" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] > 200
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_ledger_accounts`, must be a value less than or equal to `200`"
            )
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] < 1
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_ledger_accounts`, must be a value greater than or equal to `1`"
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
            "visible_in" in local_var_params
            and local_var_params["visible_in"] is not None
        ):
            query_params.append(("visible_in", local_var_params["visible_in"]))
        if (
            "not_visible_in" in local_var_params
            and local_var_params["not_visible_in"] is not None
        ):
            query_params.append(("not_visible_in", local_var_params["not_visible_in"]))
        if (
            "show_included_in_chart" in local_var_params
            and local_var_params["show_included_in_chart"] is not None
        ):
            query_params.append(
                ("show_included_in_chart", local_var_params["show_included_in_chart"])
            )
        if (
            "show_control_accounts" in local_var_params
            and local_var_params["show_control_accounts"] is not None
        ):
            query_params.append(
                ("show_control_accounts", local_var_params["show_control_accounts"])
            )
        if (
            "ledger_account_classification_id" in local_var_params
            and local_var_params["ledger_account_classification_id"] is not None
        ):
            query_params.append(
                (
                    "ledger_account_classification_id",
                    local_var_params["ledger_account_classification_id"],
                )
            )
        if (
            "show_balance_details" in local_var_params
            and local_var_params["show_balance_details"] is not None
        ):
            query_params.append(
                ("show_balance_details", local_var_params["show_balance_details"])
            )
        if (
            "exclude_deleted_entries" in local_var_params
            and local_var_params["exclude_deleted_entries"] is not None
        ):
            query_params.append(
                ("exclude_deleted_entries", local_var_params["exclude_deleted_entries"])
            )
        if (
            "from_date" in local_var_params
            and local_var_params["from_date"] is not None
        ):
            query_params.append(("from_date", local_var_params["from_date"]))
        if "to_date" in local_var_params and local_var_params["to_date"] is not None:
            query_params.append(("to_date", local_var_params["to_date"]))
        if "search" in local_var_params and local_var_params["search"] is not None:
            query_params.append(("search", local_var_params["search"]))
        if (
            "sort_order_from_user_setting" in local_var_params
            and local_var_params["sort_order_from_user_setting"] is not None
        ):
            query_params.append(
                (
                    "sort_order_from_user_setting",
                    local_var_params["sort_order_from_user_setting"],
                )
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
            "ledger_account_type_id" in local_var_params
            and local_var_params["ledger_account_type_id"] is not None
        ):
            query_params.append(
                ("ledger_account_type_id", local_var_params["ledger_account_type_id"])
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
        if (
            "_business_id" in local_var_params
            and local_var_params["_business_id"] is not None
        ):
            header_params["X-Business"] = local_var_params["_business_id"]
        auth_settings = ["OAuth2"]
        return self.api_client.call_api(
            "/ledger_accounts",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[LedgerAccount]",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_ledger_accounts_key(self, key, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_ledger_accounts_key_with_http_info(key, **kwargs)

    def get_ledger_accounts_key_with_http_info(self, key, **kwargs):
        local_var_params = locals()
        all_params = [
            "key",
            "nested_attributes",
            "show_balance_details",
            "exclude_deleted_entries",
            "from_date",
            "to_date",
            "attributes",
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
                    " to method get_ledger_accounts_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `get_ledger_accounts_key`"
            )
        collection_formats = {}
        path_params = {}
        if "key" in local_var_params:
            path_params["key"] = local_var_params["key"]
        query_params = []
        if (
            "nested_attributes" in local_var_params
            and local_var_params["nested_attributes"] is not None
        ):
            query_params.append(
                ("nested_attributes", local_var_params["nested_attributes"])
            )
        if (
            "show_balance_details" in local_var_params
            and local_var_params["show_balance_details"] is not None
        ):
            query_params.append(
                ("show_balance_details", local_var_params["show_balance_details"])
            )
        if (
            "exclude_deleted_entries" in local_var_params
            and local_var_params["exclude_deleted_entries"] is not None
        ):
            query_params.append(
                ("exclude_deleted_entries", local_var_params["exclude_deleted_entries"])
            )
        if (
            "from_date" in local_var_params
            and local_var_params["from_date"] is not None
        ):
            query_params.append(("from_date", local_var_params["from_date"]))
        if "to_date" in local_var_params and local_var_params["to_date"] is not None:
            query_params.append(("to_date", local_var_params["to_date"]))
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
            "/ledger_accounts/{key}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="LedgerAccount",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_ledger_accounts(self, ledger_accounts, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.post_ledger_accounts_with_http_info(ledger_accounts, **kwargs)

    def post_ledger_accounts_with_http_info(self, ledger_accounts, **kwargs):
        local_var_params = locals()
        all_params = ["ledger_accounts"]
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
                    " to method post_ledger_accounts" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "ledger_accounts" not in local_var_params
            or local_var_params["ledger_accounts"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `ledger_accounts` when calling `post_ledger_accounts`"
            )
        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None
        if "ledger_accounts" in local_var_params:
            body_params = local_var_params["ledger_accounts"]
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
            "/ledger_accounts",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="LedgerAccount",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_ledger_accounts_key(self, key, ledger_accounts, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.put_ledger_accounts_key_with_http_info(
            key, ledger_accounts, **kwargs
        )

    def put_ledger_accounts_key_with_http_info(self, key, ledger_accounts, **kwargs):
        local_var_params = locals()
        all_params = ["key", "ledger_accounts"]
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
                    " to method put_ledger_accounts_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `put_ledger_accounts_key`"
            )
        if self.api_client.client_side_validation and (
            "ledger_accounts" not in local_var_params
            or local_var_params["ledger_accounts"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `ledger_accounts` when calling `put_ledger_accounts_key`"
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
        if "ledger_accounts" in local_var_params:
            body_params = local_var_params["ledger_accounts"]
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
            "/ledger_accounts/{key}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="LedgerAccount",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
