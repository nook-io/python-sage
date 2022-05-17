# sage.CorrectiveReasonCodesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_corrective_reason_codes**](CorrectiveReasonCodesApi.md#get_corrective_reason_codes) | **GET** /corrective_reason_codes | Returns all Corrective Reason Codes
[**get_corrective_reason_codes_key**](CorrectiveReasonCodesApi.md#get_corrective_reason_codes_key) | **GET** /corrective_reason_codes/{key} | Returns a Corrective Reason Code


# **get_corrective_reason_codes**
> list[Base] get_corrective_reason_codes(items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Corrective Reason Codes

### Endpoint Availability  * Accounting Plus: 🇪🇸 * Accounting Standard: 🇪🇸 * Accounting Start: 🇪🇸

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
    api_instance = sage.CorrectiveReasonCodesApi(api_client)
    items_per_page = 20 # int | Returns the given number of Corrective Reason Codes per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Corrective Reason Codes (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Corrective Reason Codes (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Corrective Reason Codes
        api_response = api_instance.get_corrective_reason_codes(items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorrectiveReasonCodesApi->get_corrective_reason_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Corrective Reason Codes per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Corrective Reason Codes | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Corrective Reason Codes (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[Base]**](Base.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Corrective Reason Codes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corrective_reason_codes_key**
> Base get_corrective_reason_codes_key(key, attributes=attributes)

Returns a Corrective Reason Code

### Endpoint Availability  * Accounting Plus: 🇪🇸 * Accounting Standard: 🇪🇸 * Accounting Start: 🇪🇸

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
    api_instance = sage.CorrectiveReasonCodesApi(api_client)
    key = 'key_example' # str | The Corrective Reason Code Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Corrective Reason Code (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Corrective Reason Code
        api_response = api_instance.get_corrective_reason_codes_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorrectiveReasonCodesApi->get_corrective_reason_codes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Corrective Reason Code Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Corrective Reason Code (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**Base**](Base.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Corrective Reason Code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

