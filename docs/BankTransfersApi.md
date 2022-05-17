# sage.BankTransfersApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bank_transfers_key**](BankTransfersApi.md#delete_bank_transfers_key) | **DELETE** /bank_transfers/{key} | Deletes a Bank Transfer
[**get_bank_transfers**](BankTransfersApi.md#get_bank_transfers) | **GET** /bank_transfers | Returns all Bank Transfers
[**get_bank_transfers_key**](BankTransfersApi.md#get_bank_transfers_key) | **GET** /bank_transfers/{key} | Returns a Bank Transfer
[**post_bank_transfers**](BankTransfersApi.md#post_bank_transfers) | **POST** /bank_transfers | Creates a Bank Transfer
[**put_bank_transfers_key**](BankTransfersApi.md#put_bank_transfers_key) | **PUT** /bank_transfers/{key} | Updates a Bank Transfer


# **delete_bank_transfers_key**
> delete_bank_transfers_key(key)

Deletes a Bank Transfer

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access

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
    api_instance = sage.BankTransfersApi(api_client)
    key = 'key_example' # str | The Bank Transfer Key.

    try:
        # Deletes a Bank Transfer
        api_instance.delete_bank_transfers_key(key)
    except ApiException as e:
        print("Exception when calling BankTransfersApi->delete_bank_transfers_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Bank Transfer Key. | 

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
**204** | Deletes a Bank Transfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfers**
> list[BankTransfer] get_bank_transfers(updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, from_date=from_date, to_date=to_date, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Bank Transfers

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.BankTransfersApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Bank Transfers changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Bank Transfers deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Bank Transfers dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Bank Transfers dates (optional)
items_per_page = 20 # int | Returns the given number of Bank Transfers per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Bank Transfers (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Bank Transfers (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Bank Transfers
        api_response = api_instance.get_bank_transfers(updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, from_date=from_date, to_date=to_date, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankTransfersApi->get_bank_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Bank Transfers changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Bank Transfers deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **from_date** | **datetime**| Use this to filter by Bank Transfers dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Bank Transfers dates | [optional] 
 **items_per_page** | **int**| Returns the given number of Bank Transfers per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Bank Transfers | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Bank Transfers (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[BankTransfer]**](BankTransfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Bank Transfers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfers_key**
> BankTransfer get_bank_transfers_key(key, nested_attributes=nested_attributes, attributes=attributes)

Returns a Bank Transfer

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.BankTransfersApi(api_client)
    key = 'key_example' # str | The Bank Transfer Key.
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Bank Transfer (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Bank Transfer (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Bank Transfer
        api_response = api_instance.get_bank_transfers_key(key, nested_attributes=nested_attributes, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankTransfersApi->get_bank_transfers_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Bank Transfer Key. | 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Bank Transfer (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Bank Transfer (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**BankTransfer**](BankTransfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Bank Transfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bank_transfers**
> BankTransfer post_bank_transfers(bank_transfers)

Creates a Bank Transfer

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access, Restricted Access

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
    api_instance = sage.BankTransfersApi(api_client)
    bank_transfers = sage.PostBankTransfers() # PostBankTransfers | 

    try:
        # Creates a Bank Transfer
        api_response = api_instance.post_bank_transfers(bank_transfers)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankTransfersApi->post_bank_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfers** | [**PostBankTransfers**](PostBankTransfers.md)|  | 

### Return type

[**BankTransfer**](BankTransfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Bank Transfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bank_transfers_key**
> BankTransfer put_bank_transfers_key(key, bank_transfers)

Updates a Bank Transfer

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access, Restricted Access

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
    api_instance = sage.BankTransfersApi(api_client)
    key = 'key_example' # str | The Bank Transfer Key.
bank_transfers = sage.PutBankTransfers() # PutBankTransfers | 

    try:
        # Updates a Bank Transfer
        api_response = api_instance.put_bank_transfers_key(key, bank_transfers)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankTransfersApi->put_bank_transfers_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Bank Transfer Key. | 
 **bank_transfers** | [**PutBankTransfers**](PutBankTransfers.md)|  | 

### Return type

[**BankTransfer**](BankTransfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Bank Transfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

