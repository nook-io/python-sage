# sage.TaxOfficesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tax_offices**](TaxOfficesApi.md#get_tax_offices) | **GET** /tax_offices | Returns all Tax Offices
[**get_tax_offices_key**](TaxOfficesApi.md#get_tax_offices_key) | **GET** /tax_offices/{key} | Returns a Tax Office


# **get_tax_offices**
> list[TaxOffice] get_tax_offices(items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Tax Offices

### Endpoint Availability  * Accounting Plus: 🇩🇪 * Accounting Standard: 🇩🇪 * Accounting Start: 🇩🇪

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
    api_instance = sage.TaxOfficesApi(api_client)
    items_per_page = 20 # int | Returns the given number of Tax Offices per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Tax Offices (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Offices (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Tax Offices
        api_response = api_instance.get_tax_offices(items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxOfficesApi->get_tax_offices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Tax Offices per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Tax Offices | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Offices (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[TaxOffice]**](TaxOffice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Tax Offices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_offices_key**
> TaxOffice get_tax_offices_key(key, attributes=attributes)

Returns a Tax Office

### Endpoint Availability  * Accounting Plus: 🇩🇪 * Accounting Standard: 🇩🇪 * Accounting Start: 🇩🇪

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
    api_instance = sage.TaxOfficesApi(api_client)
    key = 'key_example' # str | The Tax Office Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Office (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Tax Office
        api_response = api_instance.get_tax_offices_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxOfficesApi->get_tax_offices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Tax Office Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Office (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**TaxOffice**](TaxOffice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Tax Office |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

