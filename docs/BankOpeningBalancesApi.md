# sage.BankOpeningBalancesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bank_opening_balances_key**](BankOpeningBalancesApi.md#delete_bank_opening_balances_key) | **DELETE** /bank_opening_balances/{key} | Deletes a Bank Opening Balance
[**get_bank_opening_balances**](BankOpeningBalancesApi.md#get_bank_opening_balances) | **GET** /bank_opening_balances | Returns all Bank Opening Balances
[**get_bank_opening_balances_key**](BankOpeningBalancesApi.md#get_bank_opening_balances_key) | **GET** /bank_opening_balances/{key} | Returns a Bank Opening Balance
[**post_bank_opening_balances**](BankOpeningBalancesApi.md#post_bank_opening_balances) | **POST** /bank_opening_balances | Creates a Bank Opening Balance
[**put_bank_opening_balances_key**](BankOpeningBalancesApi.md#put_bank_opening_balances_key) | **PUT** /bank_opening_balances/{key} | Updates a Bank Opening Balance


# **delete_bank_opening_balances_key**
> delete_bank_opening_balances_key(key)

Deletes a Bank Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings` and `Bank`: Full Access

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
    api_instance = sage.BankOpeningBalancesApi(api_client)
    key = 'key_example' # str | The Bank Opening Balance Key.

    try:
        # Deletes a Bank Opening Balance
        api_instance.delete_bank_opening_balances_key(key)
    except ApiException as e:
        print("Exception when calling BankOpeningBalancesApi->delete_bank_opening_balances_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Bank Opening Balance Key. | 

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
**204** | Deletes a Bank Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_opening_balances**
> list[BankOpeningBalance] get_bank_opening_balances(updated_or_created_since=updated_or_created_since, bank_account_id=bank_account_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Bank Opening Balances

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings` and `Bank`: Full Access, Read Only

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
    api_instance = sage.BankOpeningBalancesApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Bank Opening Balances changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
bank_account_id = 'bank_account_id_example' # str | Use this to filter by bank account id (optional)
items_per_page = 20 # int | Returns the given number of Bank Opening Balances per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Bank Opening Balances (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Bank Opening Balances (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Bank Opening Balances
        api_response = api_instance.get_bank_opening_balances(updated_or_created_since=updated_or_created_since, bank_account_id=bank_account_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankOpeningBalancesApi->get_bank_opening_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Bank Opening Balances changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **bank_account_id** | **str**| Use this to filter by bank account id | [optional] 
 **items_per_page** | **int**| Returns the given number of Bank Opening Balances per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Bank Opening Balances | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Bank Opening Balances (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[BankOpeningBalance]**](BankOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Bank Opening Balances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_opening_balances_key**
> BankOpeningBalance get_bank_opening_balances_key(key, attributes=attributes)

Returns a Bank Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings` and `Bank`: Full Access, Read Only

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
    api_instance = sage.BankOpeningBalancesApi(api_client)
    key = 'key_example' # str | The Bank Opening Balance Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Bank Opening Balance (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Bank Opening Balance
        api_response = api_instance.get_bank_opening_balances_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankOpeningBalancesApi->get_bank_opening_balances_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Bank Opening Balance Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Bank Opening Balance (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**BankOpeningBalance**](BankOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Bank Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bank_opening_balances**
> BankOpeningBalance post_bank_opening_balances(bank_opening_balances)

Creates a Bank Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings` and `Bank`: Full Access

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
    api_instance = sage.BankOpeningBalancesApi(api_client)
    bank_opening_balances = sage.PostBankOpeningBalances() # PostBankOpeningBalances | 

    try:
        # Creates a Bank Opening Balance
        api_response = api_instance.post_bank_opening_balances(bank_opening_balances)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankOpeningBalancesApi->post_bank_opening_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_opening_balances** | [**PostBankOpeningBalances**](PostBankOpeningBalances.md)|  | 

### Return type

[**BankOpeningBalance**](BankOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Bank Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bank_opening_balances_key**
> BankOpeningBalance put_bank_opening_balances_key(key, bank_opening_balances)

Updates a Bank Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings` and `Bank`: Full Access

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
    api_instance = sage.BankOpeningBalancesApi(api_client)
    key = 'key_example' # str | The Bank Opening Balance Key.
bank_opening_balances = sage.PutBankOpeningBalances() # PutBankOpeningBalances | 

    try:
        # Updates a Bank Opening Balance
        api_response = api_instance.put_bank_opening_balances_key(key, bank_opening_balances)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankOpeningBalancesApi->put_bank_opening_balances_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Bank Opening Balance Key. | 
 **bank_opening_balances** | [**PutBankOpeningBalances**](PutBankOpeningBalances.md)|  | 

### Return type

[**BankOpeningBalance**](BankOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Bank Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

