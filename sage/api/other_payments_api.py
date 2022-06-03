# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sage.api_client import ApiClient
from sage.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OtherPaymentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_other_payments_key(self, key, **kwargs):  # noqa: E501
        """Deletes a Other Payment  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_other_payments_key(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: The Other Payment Key. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_other_payments_key_with_http_info(key, **kwargs)  # noqa: E501

    def delete_other_payments_key_with_http_info(self, key, **kwargs):  # noqa: E501
        """Deletes a Other Payment  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_other_payments_key_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: The Other Payment Key. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'key'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_business_id'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_other_payments_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in local_var_params or  # noqa: E501
                                                        local_var_params['key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key` when calling `delete_other_payments_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["OAuth2"]  # noqa: E501

        return self.api_client.call_api(
            '/other_payments/{key}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_other_payments(self, **kwargs):  # noqa: E501
        """Returns all Other Payments  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Read Only, Restricted Access, Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_other_payments(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str bank_account_id: Use this to filter by bank account id
        :param str contact_id: Use this to filter by contact id
        :param datetime deleted_since: Use this to limit the response to Payments deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp.
        :param datetime from_date: Use this to filter by Payments dates
        :param bool has_attachments: Use this to filter Payments by whether they have attachments or not
        :param datetime to_date: Use this to filter by Payments dates
        :param str transaction_type_id: Use this to filter by transaction type id
        :param datetime updated_or_created_since: Use this to limit the response to Payments changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp.
        :param int items_per_page: Returns the given number of Payments per request.
        :param int page: Go to specific page of Payments
        :param str attributes: Specify the attributes that you want to expose for the Payments (expose all attributes with 'all'). These are in addition to the base attributes (name, path)
        :param str sort: Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date  Example: `sort=created_at` or `sort=created_at:desc`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[OtherPayment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_other_payments_with_http_info(**kwargs)  # noqa: E501

    def get_other_payments_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all Other Payments  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Read Only, Restricted Access, Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_other_payments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str bank_account_id: Use this to filter by bank account id
        :param str contact_id: Use this to filter by contact id
        :param datetime deleted_since: Use this to limit the response to Payments deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp.
        :param datetime from_date: Use this to filter by Payments dates
        :param bool has_attachments: Use this to filter Payments by whether they have attachments or not
        :param datetime to_date: Use this to filter by Payments dates
        :param str transaction_type_id: Use this to filter by transaction type id
        :param datetime updated_or_created_since: Use this to limit the response to Payments changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp.
        :param int items_per_page: Returns the given number of Payments per request.
        :param int page: Go to specific page of Payments
        :param str attributes: Specify the attributes that you want to expose for the Payments (expose all attributes with 'all'). These are in addition to the base attributes (name, path)
        :param str sort: Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date  Example: `sort=created_at` or `sort=created_at:desc`
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[OtherPayment], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'bank_account_id',
            'contact_id',
            'deleted_since',
            'from_date',
            'has_attachments',
            'to_date',
            'transaction_type_id',
            'updated_or_created_since',
            'items_per_page',
            'page',
            'attributes',
            'sort'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_business_id'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_other_payments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'items_per_page' in local_var_params and local_var_params['items_per_page'] > 200:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `items_per_page` when calling `get_other_payments`, must be a value less than or equal to `200`")  # noqa: E501
        if self.api_client.client_side_validation and 'items_per_page' in local_var_params and local_var_params['items_per_page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `items_per_page` when calling `get_other_payments`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bank_account_id' in local_var_params and local_var_params['bank_account_id'] is not None:  # noqa: E501
            query_params.append(('bank_account_id', local_var_params['bank_account_id']))  # noqa: E501
        if 'contact_id' in local_var_params and local_var_params['contact_id'] is not None:  # noqa: E501
            query_params.append(('contact_id', local_var_params['contact_id']))  # noqa: E501
        if 'deleted_since' in local_var_params and local_var_params['deleted_since'] is not None:  # noqa: E501
            query_params.append(('deleted_since', local_var_params['deleted_since']))  # noqa: E501
        if 'from_date' in local_var_params and local_var_params['from_date'] is not None:  # noqa: E501
            query_params.append(('from_date', local_var_params['from_date']))  # noqa: E501
        if 'has_attachments' in local_var_params and local_var_params['has_attachments'] is not None:  # noqa: E501
            query_params.append(('has_attachments', local_var_params['has_attachments']))  # noqa: E501
        if 'to_date' in local_var_params and local_var_params['to_date'] is not None:  # noqa: E501
            query_params.append(('to_date', local_var_params['to_date']))  # noqa: E501
        if 'transaction_type_id' in local_var_params and local_var_params['transaction_type_id'] is not None:  # noqa: E501
            query_params.append(('transaction_type_id', local_var_params['transaction_type_id']))  # noqa: E501
        if 'updated_or_created_since' in local_var_params and local_var_params['updated_or_created_since'] is not None:  # noqa: E501
            query_params.append(('updated_or_created_since', local_var_params['updated_or_created_since']))  # noqa: E501
        if 'items_per_page' in local_var_params and local_var_params['items_per_page'] is not None:  # noqa: E501
            query_params.append(('items_per_page', local_var_params['items_per_page']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'attributes' in local_var_params and local_var_params['attributes'] is not None:  # noqa: E501
            query_params.append(('attributes', local_var_params['attributes']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        if '_business_id' in local_var_params and local_var_params['_business_id'] is not None:  # noqa: E501
            header_params['X-Business'] = local_var_params['_business_id']

        # Authentication setting
        auth_settings = ["OAuth2"]  # noqa: E501

        return self.api_client.call_api(
            '/other_payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[OtherPayment]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_other_payments_key(self, key, **kwargs):  # noqa: E501
        """Returns a Other Payment  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Read Only, Restricted Access, Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_other_payments_key(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: The Other Payment Key. (required)
        :param str nested_attributes: Specify the attributes that you want to expose for nested entities of the Payment (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path)
        :param str attributes: Specify the attributes that you want to expose for the Payment (expose all attributes with 'all'). These are in addition to the base attributes (name, path)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: OtherPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_other_payments_key_with_http_info(key, **kwargs)  # noqa: E501

    def get_other_payments_key_with_http_info(self, key, **kwargs):  # noqa: E501
        """Returns a Other Payment  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Read Only, Restricted Access, Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_other_payments_key_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: The Other Payment Key. (required)
        :param str nested_attributes: Specify the attributes that you want to expose for nested entities of the Payment (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path)
        :param str attributes: Specify the attributes that you want to expose for the Payment (expose all attributes with 'all'). These are in addition to the base attributes (name, path)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(OtherPayment, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'key',
            'nested_attributes',
            'attributes'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_business_id'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_other_payments_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in local_var_params or  # noqa: E501
                                                        local_var_params['key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key` when calling `get_other_payments_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []
        if 'nested_attributes' in local_var_params and local_var_params['nested_attributes'] is not None:  # noqa: E501
            query_params.append(('nested_attributes', local_var_params['nested_attributes']))  # noqa: E501
        if 'attributes' in local_var_params and local_var_params['attributes'] is not None:  # noqa: E501
            query_params.append(('attributes', local_var_params['attributes']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        if '_business_id' in local_var_params and local_var_params['_business_id'] is not None:  # noqa: E501
            header_params['X-Business'] = local_var_params['_business_id']

        # Authentication setting
        auth_settings = ["OAuth2"]  # noqa: E501

        return self.api_client.call_api(
            '/other_payments/{key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OtherPayment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_other_payments(self, other_payments, **kwargs):  # noqa: E501
        """Creates a Other Payment  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Restricted Access, Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_other_payments(other_payments, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param PostOtherPayments other_payments: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: OtherPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_other_payments_with_http_info(other_payments, **kwargs)  # noqa: E501

    def post_other_payments_with_http_info(self, other_payments, **kwargs):  # noqa: E501
        """Creates a Other Payment  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Restricted Access, Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_other_payments_with_http_info(other_payments, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param PostOtherPayments other_payments: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(OtherPayment, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'other_payments'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_business_id'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_other_payments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'other_payments' is set
        if self.api_client.client_side_validation and ('other_payments' not in local_var_params or  # noqa: E501
                                                        local_var_params['other_payments'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `other_payments` when calling `post_other_payments`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'other_payments' in local_var_params:
            body_params = local_var_params['other_payments']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        if '_business_id' in local_var_params and local_var_params['_business_id'] is not None:  # noqa: E501
            header_params['X-Business'] = local_var_params['_business_id']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ["OAuth2"]  # noqa: E501

        return self.api_client.call_api(
            '/other_payments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OtherPayment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_other_payments_key(self, key, other_payments, **kwargs):  # noqa: E501
        """Updates a Other Payment  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Restricted Access, Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_other_payments_key(key, other_payments, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: The Other Payment Key. (required)
        :param PutOtherPayments other_payments: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: OtherPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.put_other_payments_key_with_http_info(key, other_payments, **kwargs)  # noqa: E501

    def put_other_payments_key_with_http_info(self, key, other_payments, **kwargs):  # noqa: E501
        """Updates a Other Payment  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Restricted Access, Full Access  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_other_payments_key_with_http_info(key, other_payments, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: The Other Payment Key. (required)
        :param PutOtherPayments other_payments: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(OtherPayment, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'key',
            'other_payments'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_business_id'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_other_payments_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in local_var_params or  # noqa: E501
                                                        local_var_params['key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key` when calling `put_other_payments_key`")  # noqa: E501
        # verify the required parameter 'other_payments' is set
        if self.api_client.client_side_validation and ('other_payments' not in local_var_params or  # noqa: E501
                                                        local_var_params['other_payments'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `other_payments` when calling `put_other_payments_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'other_payments' in local_var_params:
            body_params = local_var_params['other_payments']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        if '_business_id' in local_var_params and local_var_params['_business_id'] is not None:  # noqa: E501
            header_params['X-Business'] = local_var_params['_business_id']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ["OAuth2"]  # noqa: E501

        return self.api_client.call_api(
            '/other_payments/{key}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OtherPayment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
