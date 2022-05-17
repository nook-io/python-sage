# sage.EUSalesDescriptionsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_eu_sales_descriptions**](EUSalesDescriptionsApi.md#get_eu_sales_descriptions) | **GET** /eu_sales_descriptions | Returns all EU Sales Descriptions
[**get_eu_sales_descriptions_key**](EUSalesDescriptionsApi.md#get_eu_sales_descriptions_key) | **GET** /eu_sales_descriptions/{key} | Returns a EU Sales Description


# **get_eu_sales_descriptions**
> list[EuSalesDescription] get_eu_sales_descriptions(items_per_page=items_per_page, page=page, attributes=attributes)

Returns all EU Sales Descriptions

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
    api_instance = sage.EUSalesDescriptionsApi(api_client)
    items_per_page = 20 # int | Returns the given number of Ec Sales Descriptions per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Ec Sales Descriptions (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ec Sales Descriptions (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all EU Sales Descriptions
        api_response = api_instance.get_eu_sales_descriptions(items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EUSalesDescriptionsApi->get_eu_sales_descriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Ec Sales Descriptions per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Ec Sales Descriptions | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Ec Sales Descriptions (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[EuSalesDescription]**](EuSalesDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all EU Sales Descriptions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eu_sales_descriptions_key**
> EuSalesDescription get_eu_sales_descriptions_key(key, attributes=attributes)

Returns a EU Sales Description

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
    api_instance = sage.EUSalesDescriptionsApi(api_client)
    key = 'key_example' # str | The EU Sales Description Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ec Sales Description (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a EU Sales Description
        api_response = api_instance.get_eu_sales_descriptions_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EUSalesDescriptionsApi->get_eu_sales_descriptions_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The EU Sales Description Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Ec Sales Description (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**EuSalesDescription**](EuSalesDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a EU Sales Description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

