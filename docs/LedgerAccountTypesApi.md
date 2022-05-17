# sage.LedgerAccountTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ledger_account_types**](LedgerAccountTypesApi.md#get_ledger_account_types) | **GET** /ledger_account_types | Returns all Ledger Account Types
[**get_ledger_account_types_key**](LedgerAccountTypesApi.md#get_ledger_account_types_key) | **GET** /ledger_account_types/{key} | Returns a Ledger Account Type


# **get_ledger_account_types**
> list[Base] get_ledger_account_types(ledger_account_classification_id=ledger_account_classification_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Ledger Account Types

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
    api_instance = sage.LedgerAccountTypesApi(api_client)
    ledger_account_classification_id = 'ledger_account_classification_id_example' # str | Use this to filter by ledger account classification id (optional)
items_per_page = 20 # int | Returns the given number of Ledger Account Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Ledger Account Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ledger Account Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Ledger Account Types
        api_response = api_instance.get_ledger_account_types(ledger_account_classification_id=ledger_account_classification_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountTypesApi->get_ledger_account_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_account_classification_id** | **str**| Use this to filter by ledger account classification id | [optional] 
 **items_per_page** | **int**| Returns the given number of Ledger Account Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Ledger Account Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Ledger Account Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all Ledger Account Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_account_types_key**
> Base get_ledger_account_types_key(key, attributes=attributes)

Returns a Ledger Account Type

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
    api_instance = sage.LedgerAccountTypesApi(api_client)
    key = 'key_example' # str | The Ledger Account Type Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ledger Account Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Ledger Account Type
        api_response = api_instance.get_ledger_account_types_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountTypesApi->get_ledger_account_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Ledger Account Type Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Ledger Account Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a Ledger Account Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

