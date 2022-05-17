# sage.ContactOpeningBalancesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_contact_opening_balances_key**](ContactOpeningBalancesApi.md#delete_contact_opening_balances_key) | **DELETE** /contact_opening_balances/{key} | Deletes a Contact Opening Balance
[**get_contact_opening_balances**](ContactOpeningBalancesApi.md#get_contact_opening_balances) | **GET** /contact_opening_balances | Returns all Contact Opening Balances
[**get_contact_opening_balances_key**](ContactOpeningBalancesApi.md#get_contact_opening_balances_key) | **GET** /contact_opening_balances/{key} | Returns a Contact Opening Balance
[**post_contact_opening_balances**](ContactOpeningBalancesApi.md#post_contact_opening_balances) | **POST** /contact_opening_balances | Creates a Contact Opening Balance
[**put_contact_opening_balances_key**](ContactOpeningBalancesApi.md#put_contact_opening_balances_key) | **PUT** /contact_opening_balances/{key} | Updates a Contact Opening Balance


# **delete_contact_opening_balances_key**
> delete_contact_opening_balances_key(key)

Deletes a Contact Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings`, `Sales`, and `Purchases`: Full Access

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
    api_instance = sage.ContactOpeningBalancesApi(api_client)
    key = 'key_example' # str | The Contact Opening Balance Key.

    try:
        # Deletes a Contact Opening Balance
        api_instance.delete_contact_opening_balances_key(key)
    except ApiException as e:
        print("Exception when calling ContactOpeningBalancesApi->delete_contact_opening_balances_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Opening Balance Key. | 

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
**204** | Deletes a Contact Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_opening_balances**
> list[ContactOpeningBalance] get_contact_opening_balances(updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, contact_type_id=contact_type_id, contact_id=contact_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Contact Opening Balances

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings`, `Sales`, and `Purchases`: Full Access, Read Only

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
    api_instance = sage.ContactOpeningBalancesApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Batch Entries changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Batch Entries deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
contact_type_id = 'contact_type_id_example' # str | Use this to filter by contact type id (optional)
contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
items_per_page = 20 # int | Returns the given number of Batch Entries per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Batch Entries (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Batch Entries (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Contact Opening Balances
        api_response = api_instance.get_contact_opening_balances(updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, contact_type_id=contact_type_id, contact_id=contact_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactOpeningBalancesApi->get_contact_opening_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Batch Entries changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Batch Entries deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **contact_type_id** | **str**| Use this to filter by contact type id | [optional] 
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **items_per_page** | **int**| Returns the given number of Batch Entries per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Batch Entries | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Batch Entries (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[ContactOpeningBalance]**](ContactOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Contact Opening Balances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_opening_balances_key**
> ContactOpeningBalance get_contact_opening_balances_key(key, attributes=attributes)

Returns a Contact Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings`, `Sales`, and `Purchases`: Full Access, Read Only

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
    api_instance = sage.ContactOpeningBalancesApi(api_client)
    key = 'key_example' # str | The Contact Opening Balance Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Batch Entry (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Contact Opening Balance
        api_response = api_instance.get_contact_opening_balances_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactOpeningBalancesApi->get_contact_opening_balances_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Opening Balance Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Batch Entry (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**ContactOpeningBalance**](ContactOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Contact Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_contact_opening_balances**
> ContactOpeningBalance post_contact_opening_balances(contact_opening_balances)

Creates a Contact Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings`, `Sales`, and `Purchases`: Full Access

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
    api_instance = sage.ContactOpeningBalancesApi(api_client)
    contact_opening_balances = sage.PostContactOpeningBalances() # PostContactOpeningBalances | 

    try:
        # Creates a Contact Opening Balance
        api_response = api_instance.post_contact_opening_balances(contact_opening_balances)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactOpeningBalancesApi->post_contact_opening_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_opening_balances** | [**PostContactOpeningBalances**](PostContactOpeningBalances.md)|  | 

### Return type

[**ContactOpeningBalance**](ContactOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Contact Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_contact_opening_balances_key**
> ContactOpeningBalance put_contact_opening_balances_key(key, contact_opening_balances)

Updates a Contact Opening Balance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings`, `Sales`, and `Purchases`: Full Access

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
    api_instance = sage.ContactOpeningBalancesApi(api_client)
    key = 'key_example' # str | The Contact Opening Balance Key.
contact_opening_balances = sage.PutContactOpeningBalances() # PutContactOpeningBalances | 

    try:
        # Updates a Contact Opening Balance
        api_response = api_instance.put_contact_opening_balances_key(key, contact_opening_balances)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactOpeningBalancesApi->put_contact_opening_balances_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Opening Balance Key. | 
 **contact_opening_balances** | [**PutContactOpeningBalances**](PutContactOpeningBalances.md)|  | 

### Return type

[**ContactOpeningBalance**](ContactOpeningBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Contact Opening Balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

