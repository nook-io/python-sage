# sage.LedgerAccountOpeningBalancesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ledger_account_opening_balances_key**](LedgerAccountOpeningBalancesApi.md#delete_ledger_account_opening_balances_key) | **DELETE** /ledger_account_opening_balances/{key} | Deletes a Ledger Account Opening Balance
[**get_ledger_account_opening_balances**](LedgerAccountOpeningBalancesApi.md#get_ledger_account_opening_balances) | **GET** /ledger_account_opening_balances | Returns all Ledger Account Opening Balances
[**get_ledger_account_opening_balances_key**](LedgerAccountOpeningBalancesApi.md#get_ledger_account_opening_balances_key) | **GET** /ledger_account_opening_balances/{key} | Returns a Ledger Account Opening Balance
[**post_ledger_account_opening_balances**](LedgerAccountOpeningBalancesApi.md#post_ledger_account_opening_balances) | **POST** /ledger_account_opening_balances | Creates a Ledger Account Opening Balance
[**put_ledger_account_opening_balances_key**](LedgerAccountOpeningBalancesApi.md#put_ledger_account_opening_balances_key) | **PUT** /ledger_account_opening_balances/{key} | Updates a Ledger Account Opening Balance


# **delete_ledger_account_opening_balances_key**
> delete_ledger_account_opening_balances_key(key)

Deletes a Ledger Account Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, `Contacts`, `Journals`, `Settings`, `Bank`, `Statutory Reporting`, `Products & Services`, and `Reporting`: Full Access

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
    api_instance = sage.LedgerAccountOpeningBalancesApi(api_client)
    key = 'key_example' # str | The Ledger Account Opening Balance Key.

    try:
        # Deletes a Ledger Account Opening Balance
        api_instance.delete_ledger_account_opening_balances_key(key)
    except ApiException as e:
        print("Exception when calling LedgerAccountOpeningBalancesApi->delete_ledger_account_opening_balances_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Ledger Account Opening Balance Key. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deletes a Ledger Account Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_account_opening_balances**
> list[LedgerAccountOpeningBalance] get_ledger_account_opening_balances(updated_or_created_since=updated_or_created_since, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Ledger Account Opening Balances

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, `Contacts`, `Journals`, `Settings`, `Bank`, `Statutory Reporting`, `Products & Services`, and `Reporting`: Full Access, Read Only

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
    api_instance = sage.LedgerAccountOpeningBalancesApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Journal Opening Balance Lines changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
items_per_page = 20 # int | Returns the given number of Journal Opening Balance Lines per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Journal Opening Balance Lines (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Journal Opening Balance Lines (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Ledger Account Opening Balances
        api_response = api_instance.get_ledger_account_opening_balances(updated_or_created_since=updated_or_created_since, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountOpeningBalancesApi->get_ledger_account_opening_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Journal Opening Balance Lines changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **items_per_page** | **int**| Returns the given number of Journal Opening Balance Lines per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Journal Opening Balance Lines | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Journal Opening Balance Lines (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[LedgerAccountOpeningBalance]**](LedgerAccountOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Ledger Account Opening Balances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_account_opening_balances_key**
> LedgerAccountOpeningBalance get_ledger_account_opening_balances_key(key, attributes=attributes)

Returns a Ledger Account Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, `Contacts`, `Journals`, `Settings`, `Bank`, `Statutory Reporting`, `Products & Services`, and `Reporting`: Full Access, Read Only

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
    api_instance = sage.LedgerAccountOpeningBalancesApi(api_client)
    key = 'key_example' # str | The Ledger Account Opening Balance Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Journal Opening Balance Line (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Ledger Account Opening Balance
        api_response = api_instance.get_ledger_account_opening_balances_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountOpeningBalancesApi->get_ledger_account_opening_balances_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Ledger Account Opening Balance Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Journal Opening Balance Line (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**LedgerAccountOpeningBalance**](LedgerAccountOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Ledger Account Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ledger_account_opening_balances**
> LedgerAccountOpeningBalance post_ledger_account_opening_balances(ledger_account_opening_balances)

Creates a Ledger Account Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, `Contacts`, `Journals`, `Settings`, `Bank`, `Statutory Reporting`, `Products & Services`, and `Reporting`: Full Access

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
    api_instance = sage.LedgerAccountOpeningBalancesApi(api_client)
    ledger_account_opening_balances = sage.PostLedgerAccountOpeningBalances() # PostLedgerAccountOpeningBalances | 

    try:
        # Creates a Ledger Account Opening Balance
        api_response = api_instance.post_ledger_account_opening_balances(ledger_account_opening_balances)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountOpeningBalancesApi->post_ledger_account_opening_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_account_opening_balances** | [**PostLedgerAccountOpeningBalances**](PostLedgerAccountOpeningBalances.md)|  | 

### Return type

[**LedgerAccountOpeningBalance**](LedgerAccountOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Ledger Account Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ledger_account_opening_balances_key**
> LedgerAccountOpeningBalance put_ledger_account_opening_balances_key(key, ledger_account_opening_balances)

Updates a Ledger Account Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, `Contacts`, `Journals`, `Settings`, `Bank`, `Statutory Reporting`, `Products & Services`, and `Reporting`: Full Access

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
    api_instance = sage.LedgerAccountOpeningBalancesApi(api_client)
    key = 'key_example' # str | The Ledger Account Opening Balance Key.
ledger_account_opening_balances = sage.PutLedgerAccountOpeningBalances() # PutLedgerAccountOpeningBalances | 

    try:
        # Updates a Ledger Account Opening Balance
        api_response = api_instance.put_ledger_account_opening_balances_key(key, ledger_account_opening_balances)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountOpeningBalancesApi->put_ledger_account_opening_balances_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Ledger Account Opening Balance Key. | 
 **ledger_account_opening_balances** | [**PutLedgerAccountOpeningBalances**](PutLedgerAccountOpeningBalances.md)|  | 

### Return type

[**LedgerAccountOpeningBalance**](LedgerAccountOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Ledger Account Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

