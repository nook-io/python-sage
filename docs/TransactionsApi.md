# sage.TransactionsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /transactions | Returns all Transactions
[**get_transactions_key**](TransactionsApi.md#get_transactions_key) | **GET** /transactions/{key} | Returns a Transaction


# **get_transactions**
> list[Transaction] get_transactions(updated_or_created_since=updated_or_created_since, from_date=from_date, to_date=to_date, updated_from_date=updated_from_date, updated_to_date=updated_to_date, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, transaction_type_id=transaction_type_id)

Returns all Transactions

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
    api_instance = sage.TransactionsApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Transactions changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Transactions dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Transactions dates (optional)
updated_from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter Transactions by the date they were last updated (optional)
updated_to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter Transactions by the date they were last updated (optional)
has_attachments = True # bool | Use this to filter Transactions by whether they have attachments or not (optional)
items_per_page = 20 # int | Returns the given number of Transactions per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Transactions (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Transactions (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
transaction_type_id = 'transaction_type_id_example' # str | Use this to filter by transaction type id (optional)

    try:
        # Returns all Transactions
        api_response = api_instance.get_transactions(updated_or_created_since=updated_or_created_since, from_date=from_date, to_date=to_date, updated_from_date=updated_from_date, updated_to_date=updated_to_date, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, transaction_type_id=transaction_type_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Transactions changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **from_date** | **datetime**| Use this to filter by Transactions dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Transactions dates | [optional] 
 **updated_from_date** | **datetime**| Use this to filter Transactions by the date they were last updated | [optional] 
 **updated_to_date** | **datetime**| Use this to filter Transactions by the date they were last updated | [optional] 
 **has_attachments** | **bool**| Use this to filter Transactions by whether they have attachments or not | [optional] 
 **items_per_page** | **int**| Returns the given number of Transactions per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Transactions | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Transactions (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **transaction_type_id** | **str**| Use this to filter by transaction type id | [optional] 

### Return type

[**list[Transaction]**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Transactions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_key**
> Transaction get_transactions_key(key, expand_origin=expand_origin, attributes=attributes)

Returns a Transaction

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
    api_instance = sage.TransactionsApi(api_client)
    key = 'key_example' # str | The Transaction Key.
expand_origin = True # bool |  (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Transaction (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Transaction
        api_response = api_instance.get_transactions_key(key, expand_origin=expand_origin, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Transaction Key. | 
 **expand_origin** | **bool**|  | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Transaction (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Transaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

