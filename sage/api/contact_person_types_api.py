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


class ContactPersonTypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_contact_person_types(self, **kwargs):  # noqa: E501
        """Returns all Contact Person Types  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contact_person_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int items_per_page: Returns the given number of Contact Types per request.
        :param int page: Go to specific page of Contact Types
        :param str attributes: Specify the attributes that you want to expose for the Contact Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ContactPersonType]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_contact_person_types_with_http_info(**kwargs)  # noqa: E501

    def get_contact_person_types_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all Contact Person Types  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contact_person_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int items_per_page: Returns the given number of Contact Types per request.
        :param int page: Go to specific page of Contact Types
        :param str attributes: Specify the attributes that you want to expose for the Contact Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ContactPersonType], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'items_per_page',
            'page',
            'attributes'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contact_person_types" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'items_per_page' in local_var_params and local_var_params['items_per_page'] > 200:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `items_per_page` when calling `get_contact_person_types`, must be a value less than or equal to `200`")  # noqa: E501
        if self.api_client.client_side_validation and 'items_per_page' in local_var_params and local_var_params['items_per_page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `items_per_page` when calling `get_contact_person_types`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'items_per_page' in local_var_params and local_var_params['items_per_page'] is not None:  # noqa: E501
            query_params.append(('items_per_page', local_var_params['items_per_page']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'attributes' in local_var_params and local_var_params['attributes'] is not None:  # noqa: E501
            query_params.append(('attributes', local_var_params['attributes']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ["OAuth2"]  # noqa: E501

        return self.api_client.call_api(
            '/contact_person_types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ContactPersonType]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_contact_person_types_key(self, key, **kwargs):  # noqa: E501
        """Returns a Contact Person Type  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contact_person_types_key(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: The Contact Person Type Key. (required)
        :param str attributes: Specify the attributes that you want to expose for the Contact Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ContactPersonType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_contact_person_types_key_with_http_info(key, **kwargs)  # noqa: E501

    def get_contact_person_types_key_with_http_info(self, key, **kwargs):  # noqa: E501
        """Returns a Contact Person Type  # noqa: E501

        ### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contact_person_types_key_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: The Contact Person Type Key. (required)
        :param str attributes: Specify the attributes that you want to expose for the Contact Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ContactPersonType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'key',
            'attributes'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contact_person_types_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in local_var_params or  # noqa: E501
                                                        local_var_params['key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key` when calling `get_contact_person_types_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []
        if 'attributes' in local_var_params and local_var_params['attributes'] is not None:  # noqa: E501
            query_params.append(('attributes', local_var_params['attributes']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ["OAuth2"]  # noqa: E501

        return self.api_client.call_api(
            '/contact_person_types/{key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactPersonType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
