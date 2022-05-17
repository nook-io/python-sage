# sage.StockItemsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_stock_items_key**](StockItemsApi.md#delete_stock_items_key) | **DELETE** /stock_items/{key} | Deletes a Stock Item
[**get_stock_items**](StockItemsApi.md#get_stock_items) | **GET** /stock_items | Returns all Stock Items
[**get_stock_items_key**](StockItemsApi.md#get_stock_items_key) | **GET** /stock_items/{key} | Returns a Stock Item
[**post_stock_items**](StockItemsApi.md#post_stock_items) | **POST** /stock_items | Creates a Stock Item
[**put_stock_items_key**](StockItemsApi.md#put_stock_items_key) | **PUT** /stock_items/{key} | Updates a Stock Item


# **delete_stock_items_key**
> delete_stock_items_key(key)

Deletes a Stock Item

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
    api_instance = sage.StockItemsApi(api_client)
    key = 'key_example' # str | The Stock Item Key.

    try:
        # Deletes a Stock Item
        api_instance.delete_stock_items_key(key)
    except ApiException as e:
        print("Exception when calling StockItemsApi->delete_stock_items_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Stock Item Key. | 

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
**204** | Deletes a Stock Item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_items**
> list[StockItem] get_stock_items(search=search, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, active=active, out_of_stock=out_of_stock, below_reorder_level=below_reorder_level, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Stock Items

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
    api_instance = sage.StockItemsApi(api_client)
    search = 'search_example' # str | Use this to filter by the item code or description. (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Stock Items changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Stock Items deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
active = True # bool | Use this to only return active or inactive items (optional)
out_of_stock = True # bool | Use this to filter by the Stock Items that are out of stock (optional)
below_reorder_level = True # bool | Use this to filter by the Stock Items that are below the reorder level (optional)
items_per_page = 20 # int | Returns the given number of Stock Items per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Stock Items (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Stock Items (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Stock Items
        api_response = api_instance.get_stock_items(search=search, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, active=active, out_of_stock=out_of_stock, below_reorder_level=below_reorder_level, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockItemsApi->get_stock_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Use this to filter by the item code or description. | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Stock Items changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Stock Items deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **active** | **bool**| Use this to only return active or inactive items | [optional] 
 **out_of_stock** | **bool**| Use this to filter by the Stock Items that are out of stock | [optional] 
 **below_reorder_level** | **bool**| Use this to filter by the Stock Items that are below the reorder level | [optional] 
 **items_per_page** | **int**| Returns the given number of Stock Items per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Stock Items | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Stock Items (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[StockItem]**](StockItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Stock Items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_items_key**
> StockItem get_stock_items_key(key, attributes=attributes)

Returns a Stock Item

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
    api_instance = sage.StockItemsApi(api_client)
    key = 'key_example' # str | The Stock Item Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Stock Item (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Stock Item
        api_response = api_instance.get_stock_items_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockItemsApi->get_stock_items_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Stock Item Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Stock Item (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**StockItem**](StockItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Stock Item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_stock_items**
> StockItem post_stock_items(stock_items)

Creates a Stock Item

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
    api_instance = sage.StockItemsApi(api_client)
    stock_items = sage.PostStockItems() # PostStockItems | 

    try:
        # Creates a Stock Item
        api_response = api_instance.post_stock_items(stock_items)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockItemsApi->post_stock_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_items** | [**PostStockItems**](PostStockItems.md)|  | 

### Return type

[**StockItem**](StockItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Stock Item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_stock_items_key**
> StockItem put_stock_items_key(key, stock_items)

Updates a Stock Item

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
    api_instance = sage.StockItemsApi(api_client)
    key = 'key_example' # str | The Stock Item Key.
stock_items = sage.PutStockItems() # PutStockItems | 

    try:
        # Updates a Stock Item
        api_response = api_instance.put_stock_items_key(key, stock_items)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StockItemsApi->put_stock_items_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Stock Item Key. | 
 **stock_items** | [**PutStockItems**](PutStockItems.md)|  | 

### Return type

[**StockItem**](StockItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Stock Item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

