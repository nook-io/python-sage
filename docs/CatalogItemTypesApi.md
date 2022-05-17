# sage.CatalogItemTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_item_types**](CatalogItemTypesApi.md#get_catalog_item_types) | **GET** /catalog_item_types | Returns all Catalog Item Types
[**get_catalog_item_types_key**](CatalogItemTypesApi.md#get_catalog_item_types_key) | **GET** /catalog_item_types/{key} | Returns a Catalog Item Type


# **get_catalog_item_types**
> list[Base] get_catalog_item_types(items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Catalog Item Types

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
    api_instance = sage.CatalogItemTypesApi(api_client)
    items_per_page = 20 # int | Returns the given number of Catalog Item Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Catalog Item Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Catalog Item Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Catalog Item Types
        api_response = api_instance.get_catalog_item_types(items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogItemTypesApi->get_catalog_item_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Catalog Item Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Catalog Item Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Catalog Item Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all Catalog Item Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_item_types_key**
> Base get_catalog_item_types_key(key, attributes=attributes)

Returns a Catalog Item Type

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
    api_instance = sage.CatalogItemTypesApi(api_client)
    key = 'key_example' # str | The Catalog Item Type Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Catalog Item Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Catalog Item Type
        api_response = api_instance.get_catalog_item_types_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CatalogItemTypesApi->get_catalog_item_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Catalog Item Type Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Catalog Item Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a Catalog Item Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

