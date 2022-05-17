# sage.TransactionTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_types**](TransactionTypesApi.md#get_transaction_types) | **GET** /transaction_types | Returns all Transaction Types
[**get_transaction_types_key**](TransactionTypesApi.md#get_transaction_types_key) | **GET** /transaction_types/{key} | Returns a Transaction Type


# **get_transaction_types**
> list[Base] get_transaction_types(valid_for_business=valid_for_business, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Transaction Types

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
    api_instance = sage.TransactionTypesApi(api_client)
    valid_for_business = True # bool | Use this to filter the transaction types to a business's locale and service (optional)
items_per_page = 20 # int | Returns the given number of Transaction Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Transaction Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Transaction Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Transaction Types
        api_response = api_instance.get_transaction_types(valid_for_business=valid_for_business, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionTypesApi->get_transaction_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valid_for_business** | **bool**| Use this to filter the transaction types to a business&#39;s locale and service | [optional] 
 **items_per_page** | **int**| Returns the given number of Transaction Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Transaction Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Transaction Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all Transaction Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_types_key**
> Base get_transaction_types_key(key, attributes=attributes)

Returns a Transaction Type

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
    api_instance = sage.TransactionTypesApi(api_client)
    key = 'key_example' # str | The Transaction Type Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Transaction Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Transaction Type
        api_response = api_instance.get_transaction_types_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionTypesApi->get_transaction_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Transaction Type Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Transaction Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a Transaction Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

