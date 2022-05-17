# sage.CoaTemplatesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coa_templates**](CoaTemplatesApi.md#get_coa_templates) | **GET** /coa_templates | Returns all Coa Templates
[**get_coa_templates_key**](CoaTemplatesApi.md#get_coa_templates_key) | **GET** /coa_templates/{key} | Returns a Coa Template


# **get_coa_templates**
> list[CoaTemplate] get_coa_templates(items_per_page=items_per_page, page=page, attributes=attributes, country_id=country_id)

Returns all Coa Templates

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
    api_instance = sage.CoaTemplatesApi(api_client)
    items_per_page = 20 # int | Returns the given number of Coa Templates per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Coa Templates (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Coa Templates (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
country_id = 'country_id_example' # str | Use this to filter by country id (optional)

    try:
        # Returns all Coa Templates
        api_response = api_instance.get_coa_templates(items_per_page=items_per_page, page=page, attributes=attributes, country_id=country_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoaTemplatesApi->get_coa_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Coa Templates per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Coa Templates | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Coa Templates (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **country_id** | **str**| Use this to filter by country id | [optional] 

### Return type

[**list[CoaTemplate]**](CoaTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Coa Templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coa_templates_key**
> CoaTemplate get_coa_templates_key(key, attributes=attributes)

Returns a Coa Template

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
    api_instance = sage.CoaTemplatesApi(api_client)
    key = 'key_example' # str | The Coa Template Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Coa Template (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Coa Template
        api_response = api_instance.get_coa_templates_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoaTemplatesApi->get_coa_templates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Coa Template Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Coa Template (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**CoaTemplate**](CoaTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Coa Template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

