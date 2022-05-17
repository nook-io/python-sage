# sage.LegalFormTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_legal_form_types**](LegalFormTypesApi.md#get_legal_form_types) | **GET** /legal_form_types | Returns all Legal Form Types
[**get_legal_form_types_key**](LegalFormTypesApi.md#get_legal_form_types_key) | **GET** /legal_form_types/{key} | Returns a Legal Form Type


# **get_legal_form_types**
> list[LegalFormType] get_legal_form_types(items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Legal Form Types

### Endpoint Availability  * Accounting Plus: 🇫🇷 * Accounting Standard: 🇫🇷 * Accounting Start: 🇫🇷

### Example

```python
from __future__ import print_function
import time
import sage
from sage.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.accounting.sage.com/v3.1
# See configuration.py for a list of all supported configuration parameters.
configuration = sage.Configuration(
    host = "https://api.accounting.sage.com/v3.1"
)


# Enter a context with an instance of the API client
with sage.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sage.LegalFormTypesApi(api_client)
    items_per_page = 20 # int | Returns the given number of Business Classifications per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Business Classifications (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Business Classifications (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Legal Form Types
        api_response = api_instance.get_legal_form_types(items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LegalFormTypesApi->get_legal_form_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Business Classifications per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Business Classifications | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Business Classifications (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[LegalFormType]**](LegalFormType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Legal Form Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_form_types_key**
> LegalFormType get_legal_form_types_key(key, attributes=attributes)

Returns a Legal Form Type

### Endpoint Availability  * Accounting Plus: 🇫🇷 * Accounting Standard: 🇫🇷 * Accounting Start: 🇫🇷

### Example

```python
from __future__ import print_function
import time
import sage
from sage.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.accounting.sage.com/v3.1
# See configuration.py for a list of all supported configuration parameters.
configuration = sage.Configuration(
    host = "https://api.accounting.sage.com/v3.1"
)


# Enter a context with an instance of the API client
with sage.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sage.LegalFormTypesApi(api_client)
    key = 'key_example' # str | The Legal Form Type Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Business Classification (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Legal Form Type
        api_response = api_instance.get_legal_form_types_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LegalFormTypesApi->get_legal_form_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Legal Form Type Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Business Classification (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**LegalFormType**](LegalFormType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Legal Form Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

