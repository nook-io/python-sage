# sage.JournalCodeTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_journal_code_types**](JournalCodeTypesApi.md#get_journal_code_types) | **GET** /journal_code_types | Returns all Journal Code Types
[**get_journal_code_types_key**](JournalCodeTypesApi.md#get_journal_code_types_key) | **GET** /journal_code_types/{key} | Returns a Journal Code Type


# **get_journal_code_types**
> list[JournalCodeType] get_journal_code_types(items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Journal Code Types

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = sage.JournalCodeTypesApi(api_client)
    items_per_page = 20 # int | Returns the given number of Country Journal Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Country Journal Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Country Journal Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Journal Code Types
        api_response = api_instance.get_journal_code_types(items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalCodeTypesApi->get_journal_code_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Country Journal Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Country Journal Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Country Journal Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[JournalCodeType]**](JournalCodeType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Journal Code Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_code_types_key**
> JournalCodeType get_journal_code_types_key(key, attributes=attributes)

Returns a Journal Code Type

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = sage.JournalCodeTypesApi(api_client)
    key = 'key_example' # str | The Journal Code Type Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Country Journal Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Journal Code Type
        api_response = api_instance.get_journal_code_types_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalCodeTypesApi->get_journal_code_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Journal Code Type Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Country Journal Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**JournalCodeType**](JournalCodeType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Journal Code Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

