# sage.StockMovementsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_stock_movements_key**](StockMovementsApi.md#delete_stock_movements_key) | **DELETE** /stock_movements/{key} | Deletes a Stock Movement
[**get_stock_movements**](StockMovementsApi.md#get_stock_movements) | **GET** /stock_movements | Returns all Stock Movements
[**get_stock_movements_key**](StockMovementsApi.md#get_stock_movements_key) | **GET** /stock_movements/{key} | Returns a Stock Movement
[**post_stock_movements**](StockMovementsApi.md#post_stock_movements) | **POST** /stock_movements | Creates a Stock Movement
[**put_stock_movements_key**](StockMovementsApi.md#put_stock_movements_key) | **PUT** /stock_movements/{key} | Updates a Stock Movement


# **delete_stock_movements_key**
> delete_stock_movements_key(key)

Deletes a Stock Movement

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Full Access

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
    api_instance = sage.StockMovementsApi(api_client)
    key = 'key_example' # str | The Stock Movement Key.

    try:
        # Deletes a Stock Movement
        api_instance.delete_stock_movements_key(key)
    except ApiException as e:
        print("Exception when calling StockMovementsApi->delete_stock_movements_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Stock Movement Key. | 

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
**204** | Deletes a Stock Movement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_movements**
> list[StockMovement] get_stock_movements(search=search, stock_item_id=stock_item_id, from_date=from_date, to_date=to_date, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Stock Movements

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.StockMovementsApi(api_client)
    search = 'search_example' # str | Use this to filter by the details (optional)
stock_item_id = 'stock_item_id_example' # str | Use this to filter  by stock_item_id (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Stock Movements dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Stock Movements dates (optional)
items_per_page = 20 # int | Returns the given number of Stock Movements per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Stock Movements (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Stock Movements (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Stock Movements
        api_response = api_instance.get_stock_movements(search=search, stock_item_id=stock_item_id, from_date=from_date, to_date=to_date, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockMovementsApi->get_stock_movements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Use this to filter by the details | [optional] 
 **stock_item_id** | **str**| Use this to filter  by stock_item_id | [optional] 
 **from_date** | **datetime**| Use this to filter by Stock Movements dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Stock Movements dates | [optional] 
 **items_per_page** | **int**| Returns the given number of Stock Movements per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Stock Movements | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Stock Movements (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[StockMovement]**](StockMovement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Stock Movements |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_movements_key**
> StockMovement get_stock_movements_key(key, attributes=attributes)

Returns a Stock Movement

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.StockMovementsApi(api_client)
    key = 'key_example' # str | The Stock Movement Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Stock Movement (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Stock Movement
        api_response = api_instance.get_stock_movements_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockMovementsApi->get_stock_movements_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Stock Movement Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Stock Movement (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**StockMovement**](StockMovement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Stock Movement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_stock_movements**
> StockMovement post_stock_movements(stock_movements)

Creates a Stock Movement

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Restricted Access, Full Access

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
    api_instance = sage.StockMovementsApi(api_client)
    stock_movements = sage.PostStockMovements() # PostStockMovements | 

    try:
        # Creates a Stock Movement
        api_response = api_instance.post_stock_movements(stock_movements)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockMovementsApi->post_stock_movements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_movements** | [**PostStockMovements**](PostStockMovements.md)|  | 

### Return type

[**StockMovement**](StockMovement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Stock Movement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_stock_movements_key**
> StockMovement put_stock_movements_key(key, stock_movements)

Updates a Stock Movement

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Full Access

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
    api_instance = sage.StockMovementsApi(api_client)
    key = 'key_example' # str | The Stock Movement Key.
stock_movements = sage.PutStockMovements() # PutStockMovements | 

    try:
        # Updates a Stock Movement
        api_response = api_instance.put_stock_movements_key(key, stock_movements)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockMovementsApi->put_stock_movements_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Stock Movement Key. | 
 **stock_movements** | [**PutStockMovements**](PutStockMovements.md)|  | 

### Return type

[**StockMovement**](StockMovement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Stock Movement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

