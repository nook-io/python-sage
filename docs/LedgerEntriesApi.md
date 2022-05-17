# sage.LedgerEntriesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ledger_entries**](LedgerEntriesApi.md#get_ledger_entries) | **GET** /ledger_entries | Returns all Ledger Entries
[**get_ledger_entries_key**](LedgerEntriesApi.md#get_ledger_entries_key) | **GET** /ledger_entries/{key} | Returns a Ledger Entry


# **get_ledger_entries**
> list[LedgerEntry] get_ledger_entries(from_date=from_date, to_date=to_date, transaction_id=transaction_id, transaction_type_id=transaction_type_id, journal_code_id=journal_code_id, updated_or_created_since=updated_or_created_since, items_per_page=items_per_page, page=page, attributes=attributes, ledger_account_id=ledger_account_id)

Returns all Ledger Entries

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Journals`: Read Only, Full Access

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
    api_instance = sage.LedgerEntriesApi(api_client)
    from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Ledger Entries dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Ledger Entries dates (optional)
transaction_id = 'transaction_id_example' # str | Use this to filter by transaction id (optional)
transaction_type_id = 'transaction_type_id_example' # str | Use this to filter by transaction type id (optional)
journal_code_id = 'journal_code_id_example' # str | Use this to filter by journal code id (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Ledger Entries changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
items_per_page = 20 # int | Returns the given number of Ledger Entries per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Ledger Entries (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ledger Entries (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
ledger_account_id = 'ledger_account_id_example' # str | Use this to filter by ledger account id (optional)

    try:
        # Returns all Ledger Entries
        api_response = api_instance.get_ledger_entries(from_date=from_date, to_date=to_date, transaction_id=transaction_id, transaction_type_id=transaction_type_id, journal_code_id=journal_code_id, updated_or_created_since=updated_or_created_since, items_per_page=items_per_page, page=page, attributes=attributes, ledger_account_id=ledger_account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerEntriesApi->get_ledger_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **datetime**| Use this to filter by Ledger Entries dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Ledger Entries dates | [optional] 
 **transaction_id** | **str**| Use this to filter by transaction id | [optional] 
 **transaction_type_id** | **str**| Use this to filter by transaction type id | [optional] 
 **journal_code_id** | **str**| Use this to filter by journal code id | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Ledger Entries changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **items_per_page** | **int**| Returns the given number of Ledger Entries per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Ledger Entries | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Ledger Entries (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **ledger_account_id** | **str**| Use this to filter by ledger account id | [optional] 

### Return type

[**list[LedgerEntry]**](LedgerEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Ledger Entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_entries_key**
> LedgerEntry get_ledger_entries_key(key, nested_attributes=nested_attributes, attributes=attributes)

Returns a Ledger Entry

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Journals`: Read Only, Full Access

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
    api_instance = sage.LedgerEntriesApi(api_client)
    key = 'key_example' # str | The Ledger Entry Key.
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Ledger Entry (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ledger Entry (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Ledger Entry
        api_response = api_instance.get_ledger_entries_key(key, nested_attributes=nested_attributes, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerEntriesApi->get_ledger_entries_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Ledger Entry Key. | 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Ledger Entry (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Ledger Entry (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**LedgerEntry**](LedgerEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Ledger Entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

