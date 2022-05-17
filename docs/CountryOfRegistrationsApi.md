# sage.CountryOfRegistrationsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries_of_registration**](CountryOfRegistrationsApi.md#get_countries_of_registration) | **GET** /countries_of_registration | Returns all Country Of Registrations
[**get_countries_of_registration_key**](CountryOfRegistrationsApi.md#get_countries_of_registration_key) | **GET** /countries_of_registration/{key} | Returns a Country Of Registration


# **get_countries_of_registration**
> list[Base] get_countries_of_registration(items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Country Of Registrations

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
    api_instance = sage.CountryOfRegistrationsApi(api_client)
    items_per_page = 20 # int | Returns the given number of Registered Countries per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Registered Countries (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Registered Countries (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Country Of Registrations
        api_response = api_instance.get_countries_of_registration(items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CountryOfRegistrationsApi->get_countries_of_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Registered Countries per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Registered Countries | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Registered Countries (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all Country Of Registrations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries_of_registration_key**
> Base get_countries_of_registration_key(key, attributes=attributes)

Returns a Country Of Registration

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
    api_instance = sage.CountryOfRegistrationsApi(api_client)
    key = 'key_example' # str | The Country Of Registration Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Registered Country (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Country Of Registration
        api_response = api_instance.get_countries_of_registration_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CountryOfRegistrationsApi->get_countries_of_registration_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Country Of Registration Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Registered Country (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a Country Of Registration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

