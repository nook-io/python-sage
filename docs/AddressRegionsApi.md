# sage.AddressRegionsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_regions**](AddressRegionsApi.md#get_address_regions) | **GET** /address_regions | Returns all Address Regions
[**get_address_regions_key**](AddressRegionsApi.md#get_address_regions_key) | **GET** /address_regions/{key} | Returns a Address Region


# **get_address_regions**
> list[AddressRegion] get_address_regions(items_per_page=items_per_page, page=page, attributes=attributes, country_id=country_id)

Returns all Address Regions

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
    api_instance = sage.AddressRegionsApi(api_client)
    items_per_page = 20 # int | Returns the given number of States per request. (optional) (default to 20)
page = 1 # int | Go to specific page of States (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the States (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
country_id = 'country_id_example' # str | Use this to filter by country id (optional)

    try:
        # Returns all Address Regions
        api_response = api_instance.get_address_regions(items_per_page=items_per_page, page=page, attributes=attributes, country_id=country_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressRegionsApi->get_address_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of States per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of States | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the States (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **country_id** | **str**| Use this to filter by country id | [optional] 

### Return type

[**list[AddressRegion]**](AddressRegion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Address Regions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_regions_key**
> AddressRegion get_address_regions_key(key, attributes=attributes)

Returns a Address Region

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
    api_instance = sage.AddressRegionsApi(api_client)
    key = 'key_example' # str | The Address Region Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the State (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Address Region
        api_response = api_instance.get_address_regions_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressRegionsApi->get_address_regions_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Address Region Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the State (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**AddressRegion**](AddressRegion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Address Region |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

