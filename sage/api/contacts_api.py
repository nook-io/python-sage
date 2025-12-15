from __future__ import absolute_import
import six
from sage.api_client import ApiClient
from sage.exceptions import ApiTypeError, ApiValueError


class ContactsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_contacts_key(self, key, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.delete_contacts_key_with_http_info(key, **kwargs)

    def delete_contacts_key_with_http_info(self, key, **kwargs):
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
                    " to method delete_contacts_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `delete_contacts_key`"
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
            "/contacts/{key}",
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

    def get_contacts(self, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_contacts_with_http_info(**kwargs)

    def get_contacts_with_http_info(self, **kwargs):
        local_var_params = locals()
        all_params = [
            "updated_or_created_since",
            "deleted_since",
            "contact_type_id",
            "exclude_system",
            "nested_attributes",
            "show_balance",
            "context_date",
            "search",
            "email",
            "show_unfinished_recurring_invoices_status",
            "items_per_page",
            "page",
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
                    " to method get_contacts" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] > 200
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_contacts`, must be a value less than or equal to `200`"
            )
        if (
            self.api_client.client_side_validation
            and "items_per_page" in local_var_params
            and local_var_params["items_per_page"] < 1
        ):
            raise ApiValueError(
                "Invalid value for parameter `items_per_page` when calling `get_contacts`, must be a value greater than or equal to `1`"
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
            "deleted_since" in local_var_params
            and local_var_params["deleted_since"] is not None
        ):
            query_params.append(("deleted_since", local_var_params["deleted_since"]))
        if (
            "contact_type_id" in local_var_params
            and local_var_params["contact_type_id"] is not None
        ):
            query_params.append(
                ("contact_type_id", local_var_params["contact_type_id"])
            )
        if (
            "exclude_system" in local_var_params
            and local_var_params["exclude_system"] is not None
        ):
            query_params.append(("exclude_system", local_var_params["exclude_system"]))
        if (
            "nested_attributes" in local_var_params
            and local_var_params["nested_attributes"] is not None
        ):
            query_params.append(
                ("nested_attributes", local_var_params["nested_attributes"])
            )
        if (
            "show_balance" in local_var_params
            and local_var_params["show_balance"] is not None
        ):
            query_params.append(("show_balance", local_var_params["show_balance"]))
        if (
            "context_date" in local_var_params
            and local_var_params["context_date"] is not None
        ):
            query_params.append(("context_date", local_var_params["context_date"]))
        if "search" in local_var_params and local_var_params["search"] is not None:
            query_params.append(("search", local_var_params["search"]))
        if "email" in local_var_params and local_var_params["email"] is not None:
            query_params.append(("email", local_var_params["email"]))
        if (
            "show_unfinished_recurring_invoices_status" in local_var_params
            and local_var_params["show_unfinished_recurring_invoices_status"]
            is not None
        ):
            query_params.append(
                (
                    "show_unfinished_recurring_invoices_status",
                    local_var_params["show_unfinished_recurring_invoices_status"],
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
            "/contacts",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[Contact]",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_contacts_key(self, key, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.get_contacts_key_with_http_info(key, **kwargs)

    def get_contacts_key_with_http_info(self, key, **kwargs):
        local_var_params = locals()
        all_params = [
            "key",
            "nested_attributes",
            "show_balance",
            "context_date",
            "show_unfinished_recurring_invoices_status",
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
                    " to method get_contacts_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `get_contacts_key`"
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
            "show_balance" in local_var_params
            and local_var_params["show_balance"] is not None
        ):
            query_params.append(("show_balance", local_var_params["show_balance"]))
        if (
            "context_date" in local_var_params
            and local_var_params["context_date"] is not None
        ):
            query_params.append(("context_date", local_var_params["context_date"]))
        if (
            "show_unfinished_recurring_invoices_status" in local_var_params
            and local_var_params["show_unfinished_recurring_invoices_status"]
            is not None
        ):
            query_params.append(
                (
                    "show_unfinished_recurring_invoices_status",
                    local_var_params["show_unfinished_recurring_invoices_status"],
                )
            )
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
            "/contacts/{key}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Contact",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_contacts(self, contacts, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.post_contacts_with_http_info(contacts, **kwargs)

    def post_contacts_with_http_info(self, contacts, **kwargs):
        local_var_params = locals()
        all_params = ["contacts"]
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
                    " to method post_contacts" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "contacts" not in local_var_params or local_var_params["contacts"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `contacts` when calling `post_contacts`"
            )
        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None
        if "contacts" in local_var_params:
            body_params = local_var_params["contacts"]
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
            "/contacts",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Contact",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_contacts_key(self, key, contacts, **kwargs):
        kwargs["_return_http_data_only"] = True
        return self.put_contacts_key_with_http_info(key, contacts, **kwargs)

    def put_contacts_key_with_http_info(self, key, contacts, **kwargs):
        local_var_params = locals()
        all_params = ["key", "contacts"]
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
                    " to method put_contacts_key" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        if self.api_client.client_side_validation and (
            "key" not in local_var_params or local_var_params["key"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `key` when calling `put_contacts_key`"
            )
        if self.api_client.client_side_validation and (
            "contacts" not in local_var_params or local_var_params["contacts"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `contacts` when calling `put_contacts_key`"
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
        if "contacts" in local_var_params:
            body_params = local_var_params["contacts"]
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
            "/contacts/{key}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Contact",
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
