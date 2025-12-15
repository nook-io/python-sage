from __future__ import absolute_import
import six
from sage.api_client import ApiClient
from sage.exceptions import ApiTypeError, ApiValueError


class SalesCorrectiveInvoicesApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_sales_corrective_invoices_key(self, key, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.delete_sales_corrective_invoices_key_with_http_info(key, **kwargs)

    def delete_sales_corrective_invoices_key_with_http_info(self, key, **kwargs):
        local_var_params = locals()
        all_params = ["key", "void_reason"]
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
                    " to method delete_sales_corrective_invoices_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `delete_sales_corrective_invoices_key`"
            )
        collection_formats = {}
        path_params = {}
        if "key" in local_var_params:
            path_params["key"] = local_var_params["key"]
        query_params = []
        if (
            "void_reason" in local_var_params
            and local_var_params["void_reason"] is not None
        ):
            query_params.append(("void_reason", local_var_params["void_reason"]))
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
            "/sales_corrective_invoices/{key}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SalesCorrectiveInvoice",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_sales_corrective_invoices(self, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_sales_corrective_invoices_with_http_info(**kwargs)

    def get_sales_corrective_invoices_with_http_info(self, **kwargs):
        local_var_params = locals()
        all_params = [
            "show_payments_allocations",
            "search",
            "contact_id",
            "status_id",
            "from_date",
            "to_date",
            "updated_or_created_since",
            "deleted_since",
            "has_attachments",
            "items_per_page",
            "page",
            "attributes",
            "sort",
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
                    " to method get_sales_corrective_invoices" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] > 200
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_sales_corrective_invoices`, must be a value less than or equal to `200`"
            )
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] < 1
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_sales_corrective_invoices`, must be a value greater than or equal to `1`"
            )
        collection_formats = {}
        path_params = {}
        query_params = []
        if (
            "show_payments_allocations" in local_var_params
            and local_var_params["show_payments_allocations"] is not None
        ):
            query_params.append(
                (
                    "show_payments_allocations",
                    local_var_params["show_payments_allocations"],
                )
            )
        if "search" in local_var_params and local_var_params["search"] is not None:
            query_params.append(("search", local_var_params["search"]))
        if (
            "contact_id" in local_var_params
            and local_var_params["contact_id"] is not None
        ):
            query_params.append(("contact_id", local_var_params["contact_id"]))
        if (
            "status_id" in local_var_params
            and local_var_params["status_id"] is not None
        ):
            query_params.append(("status_id", local_var_params["status_id"]))
        if (
            "from_date" in local_var_params
            and local_var_params["from_date"] is not None
        ):
            query_params.append(("from_date", local_var_params["from_date"]))
        if "to_date" in local_var_params and local_var_params["to_date"] is not None:
            query_params.append(("to_date", local_var_params["to_date"]))
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
            "deleted_since" in local_var_params
            and local_var_params["deleted_since"] is not None
        ):
            query_params.append(("deleted_since", local_var_params["deleted_since"]))
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
        if "sort" in local_var_params and local_var_params["sort"] is not None:
            query_params.append(("sort", local_var_params["sort"]))
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
            "/sales_corrective_invoices",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[SalesCorrectiveInvoice]",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_sales_corrective_invoices_key(self, key, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_sales_corrective_invoices_key_with_http_info(key, **kwargs)

    def get_sales_corrective_invoices_key_with_http_info(self, key, **kwargs):
        local_var_params = locals()
        all_params = [
            "key",
            "show_payments_allocations",
            "nested_attributes",
            "mark_as_sent",
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
                    " to method get_sales_corrective_invoices_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `get_sales_corrective_invoices_key`"
            )
        collection_formats = {}
        path_params = {}
        if "key" in local_var_params:
            path_params["key"] = local_var_params["key"]
        query_params = []
        if (
            "show_payments_allocations" in local_var_params
            and local_var_params["show_payments_allocations"] is not None
        ):
            query_params.append(
                (
                    "show_payments_allocations",
                    local_var_params["show_payments_allocations"],
                )
            )
        if (
            "nested_attributes" in local_var_params
            and local_var_params["nested_attributes"] is not None
        ):
            query_params.append(
                ("nested_attributes", local_var_params["nested_attributes"])
            )
        if (
            "mark_as_sent" in local_var_params
            and local_var_params["mark_as_sent"] is not None
        ):
            query_params.append(("mark_as_sent", local_var_params["mark_as_sent"]))
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
            "/sales_corrective_invoices/{key}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SalesCorrectiveInvoice",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_sales_corrective_invoices(self, sales_corrective_invoices, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.post_sales_corrective_invoices_with_http_info(
            sales_corrective_invoices, **kwargs
        )

    def post_sales_corrective_invoices_with_http_info(
        self, sales_corrective_invoices, **kwargs
    ):
        local_var_params = locals()
        all_params = ["sales_corrective_invoices"]
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
                    " to method post_sales_corrective_invoices" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "sales_corrective_invoices" not in local_var_params
            or local_var_params["sales_corrective_invoices"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `sales_corrective_invoices` when calling `post_sales_corrective_invoices`"
            )
        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None
        if "sales_corrective_invoices" in local_var_params:
            body_params = local_var_params["sales_corrective_invoices"]
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
            "/sales_corrective_invoices",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SalesCorrectiveInvoice",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_sales_corrective_invoices_key(
        self, key, sales_corrective_invoices, **kwargs
    ):
        kwargs["_return_http_data_only"] = True
        return self.put_sales_corrective_invoices_key_with_http_info(
            key, sales_corrective_invoices, **kwargs
        )

    def put_sales_corrective_invoices_key_with_http_info(
        self, key, sales_corrective_invoices, **kwargs
    ):
        local_var_params = locals()
        all_params = ["key", "sales_corrective_invoices"]
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
                    " to method put_sales_corrective_invoices_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `put_sales_corrective_invoices_key`"
            )
        if self.api_client.client_side_validation and (
            "sales_corrective_invoices" not in local_var_params
            or local_var_params["sales_corrective_invoices"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `sales_corrective_invoices` when calling `put_sales_corrective_invoices_key`"
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
        if "sales_corrective_invoices" in local_var_params:
            body_params = local_var_params["sales_corrective_invoices"]
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
            "/sales_corrective_invoices/{key}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SalesCorrectiveInvoice",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
