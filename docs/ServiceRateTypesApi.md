# sage.ServiceRateTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_rate_types_key**](ServiceRateTypesApi.md#delete_service_rate_types_key) | **DELETE** /service_rate_types/{key} | Deletes a Service Rate Type
[**get_service_rate_types**](ServiceRateTypesApi.md#get_service_rate_types) | **GET** /service_rate_types | Returns all Service Rate Types
[**get_service_rate_types_key**](ServiceRateTypesApi.md#get_service_rate_types_key) | **GET** /service_rate_types/{key} | Returns a Service Rate Type
[**post_service_rate_types**](ServiceRateTypesApi.md#post_service_rate_types) | **POST** /service_rate_types | Creates a Service Rate Type
[**put_service_rate_types_key**](ServiceRateTypesApi.md#put_service_rate_types_key) | **PUT** /service_rate_types/{key} | Updates a Service Rate Type


# **delete_service_rate_types_key**
> delete_service_rate_types_key(key)

Deletes a Service Rate Type

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Full Access

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
    api_instance = sage.ServiceRateTypesApi(api_client)
    key = 'key_example' # str | The Service Rate Type Key.

    try:
        # Deletes a Service Rate Type
        api_instance.delete_service_rate_types_key(key)
    except ApiException as e:
        print("Exception when calling ServiceRateTypesApi->delete_service_rate_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Service Rate Type Key. | 

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
**204** | Deletes a Service Rate Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_rate_types**
> list[ServiceRateType] get_service_rate_types(updated_or_created_since=updated_or_created_since, active=active, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Service Rate Types

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.ServiceRateTypesApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Service Rates changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
active = True # bool | Use this to only return active or inactive items (optional)
items_per_page = 20 # int | Returns the given number of Service Rates per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Service Rates (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Service Rates (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Service Rate Types
        api_response = api_instance.get_service_rate_types(updated_or_created_since=updated_or_created_since, active=active, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceRateTypesApi->get_service_rate_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Service Rates changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **active** | **bool**| Use this to only return active or inactive items | [optional] 
 **items_per_page** | **int**| Returns the given number of Service Rates per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Service Rates | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Service Rates (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[ServiceRateType]**](ServiceRateType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Service Rate Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_rate_types_key**
> ServiceRateType get_service_rate_types_key(key, attributes=attributes)

Returns a Service Rate Type

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.ServiceRateTypesApi(api_client)
    key = 'key_example' # str | The Service Rate Type Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Service Rate (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Service Rate Type
        api_response = api_instance.get_service_rate_types_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceRateTypesApi->get_service_rate_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Service Rate Type Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Service Rate (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**ServiceRateType**](ServiceRateType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Service Rate Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_rate_types**
> ServiceRateType post_service_rate_types(service_rate_types)

Creates a Service Rate Type

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Restricted Access, Full Access

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
    api_instance = sage.ServiceRateTypesApi(api_client)
    service_rate_types = sage.PostServiceRateTypes() # PostServiceRateTypes | 

    try:
        # Creates a Service Rate Type
        api_response = api_instance.post_service_rate_types(service_rate_types)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceRateTypesApi->post_service_rate_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_rate_types** | [**PostServiceRateTypes**](PostServiceRateTypes.md)|  | 

### Return type

[**ServiceRateType**](ServiceRateType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Service Rate Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_rate_types_key**
> ServiceRateType put_service_rate_types_key(key, service_rate_types)

Updates a Service Rate Type

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Full Access

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
    api_instance = sage.ServiceRateTypesApi(api_client)
    key = 'key_example' # str | The Service Rate Type Key.
service_rate_types = sage.PutServiceRateTypes() # PutServiceRateTypes | 

    try:
        # Updates a Service Rate Type
        api_response = api_instance.put_service_rate_types_key(key, service_rate_types)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceRateTypesApi->put_service_rate_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Service Rate Type Key. | 
 **service_rate_types** | [**PutServiceRateTypes**](PutServiceRateTypes.md)|  | 

### Return type

[**ServiceRateType**](ServiceRateType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Service Rate Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

