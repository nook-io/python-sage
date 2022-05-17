# sage.LedgerAccountClassificationsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ledger_account_classifications**](LedgerAccountClassificationsApi.md#get_ledger_account_classifications) | **GET** /ledger_account_classifications | Returns all Ledger Account Classifications
[**get_ledger_account_classifications_key**](LedgerAccountClassificationsApi.md#get_ledger_account_classifications_key) | **GET** /ledger_account_classifications/{key} | Returns a Ledger Account Classification


# **get_ledger_account_classifications**
> list[Base] get_ledger_account_classifications(ledger_account_type_id=ledger_account_type_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Ledger Account Classifications

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
    api_instance = sage.LedgerAccountClassificationsApi(api_client)
    ledger_account_type_id = 'ledger_account_type_id_example' # str | Use this to filter by ledger account type id (optional)
items_per_page = 20 # int | Returns the given number of Ledger Account Classifications per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Ledger Account Classifications (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ledger Account Classifications (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Ledger Account Classifications
        api_response = api_instance.get_ledger_account_classifications(ledger_account_type_id=ledger_account_type_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountClassificationsApi->get_ledger_account_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_account_type_id** | **str**| Use this to filter by ledger account type id | [optional] 
 **items_per_page** | **int**| Returns the given number of Ledger Account Classifications per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Ledger Account Classifications | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Ledger Account Classifications (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all Ledger Account Classifications |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_account_classifications_key**
> Base get_ledger_account_classifications_key(key, attributes=attributes)

Returns a Ledger Account Classification

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
    api_instance = sage.LedgerAccountClassificationsApi(api_client)
    key = 'key_example' # str | The Ledger Account Classification Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ledger Account Classification (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Ledger Account Classification
        api_response = api_instance.get_ledger_account_classifications_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountClassificationsApi->get_ledger_account_classifications_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Ledger Account Classification Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Ledger Account Classification (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a Ledger Account Classification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

