# sage.BusinessExchangeRatesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_business_exchange_rates_key**](BusinessExchangeRatesApi.md#delete_business_exchange_rates_key) | **DELETE** /business_exchange_rates/{key} | Deletes a Business Exchange Rate
[**get_business_exchange_rates**](BusinessExchangeRatesApi.md#get_business_exchange_rates) | **GET** /business_exchange_rates | Returns all Business Exchange Rates
[**get_business_exchange_rates_key**](BusinessExchangeRatesApi.md#get_business_exchange_rates_key) | **GET** /business_exchange_rates/{key} | Returns a Business Exchange Rate
[**post_business_exchange_rates**](BusinessExchangeRatesApi.md#post_business_exchange_rates) | **POST** /business_exchange_rates | Creates a Business Exchange Rate
[**put_business_exchange_rates_key**](BusinessExchangeRatesApi.md#put_business_exchange_rates_key) | **PUT** /business_exchange_rates/{key} | Updates a Business Exchange Rate


# **delete_business_exchange_rates_key**
> delete_business_exchange_rates_key(key)

Deletes a Business Exchange Rate

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access

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
    api_instance = sage.BusinessExchangeRatesApi(api_client)
    key = 'key_example' # str | The Business Exchange Rate Key.

    try:
        # Deletes a Business Exchange Rate
        api_instance.delete_business_exchange_rates_key(key)
    except ApiException as e:
        print("Exception when calling BusinessExchangeRatesApi->delete_business_exchange_rates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Business Exchange Rate Key. | 

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
**204** | Deletes a Business Exchange Rate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_exchange_rates**
> list[BusinessExchangeRate] get_business_exchange_rates(items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Business Exchange Rates

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access, Read Only

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
    api_instance = sage.BusinessExchangeRatesApi(api_client)
    items_per_page = 20 # int | Returns the given number of Business Exchange Rates per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Business Exchange Rates (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Business Exchange Rates (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Business Exchange Rates
        api_response = api_instance.get_business_exchange_rates(items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessExchangeRatesApi->get_business_exchange_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Business Exchange Rates per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Business Exchange Rates | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Business Exchange Rates (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[BusinessExchangeRate]**](BusinessExchangeRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Business Exchange Rates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_exchange_rates_key**
> BusinessExchangeRate get_business_exchange_rates_key(key, attributes=attributes)

Returns a Business Exchange Rate

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access, Read Only

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
    api_instance = sage.BusinessExchangeRatesApi(api_client)
    key = 'key_example' # str | The Business Exchange Rate Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Business Exchange Rate (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Business Exchange Rate
        api_response = api_instance.get_business_exchange_rates_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessExchangeRatesApi->get_business_exchange_rates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Business Exchange Rate Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Business Exchange Rate (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**BusinessExchangeRate**](BusinessExchangeRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Business Exchange Rate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_business_exchange_rates**
> BusinessExchangeRate post_business_exchange_rates(business_exchange_rates)

Creates a Business Exchange Rate

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access

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
    api_instance = sage.BusinessExchangeRatesApi(api_client)
    business_exchange_rates = sage.PostBusinessExchangeRates() # PostBusinessExchangeRates | 

    try:
        # Creates a Business Exchange Rate
        api_response = api_instance.post_business_exchange_rates(business_exchange_rates)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessExchangeRatesApi->post_business_exchange_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_exchange_rates** | [**PostBusinessExchangeRates**](PostBusinessExchangeRates.md)|  | 

### Return type

[**BusinessExchangeRate**](BusinessExchangeRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Business Exchange Rate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_business_exchange_rates_key**
> BusinessExchangeRate put_business_exchange_rates_key(key, business_exchange_rates)

Updates a Business Exchange Rate

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access

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
    api_instance = sage.BusinessExchangeRatesApi(api_client)
    key = 'key_example' # str | The Business Exchange Rate Key.
business_exchange_rates = sage.PutBusinessExchangeRates() # PutBusinessExchangeRates | 

    try:
        # Updates a Business Exchange Rate
        api_response = api_instance.put_business_exchange_rates_key(key, business_exchange_rates)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessExchangeRatesApi->put_business_exchange_rates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Business Exchange Rate Key. | 
 **business_exchange_rates** | [**PutBusinessExchangeRates**](PutBusinessExchangeRates.md)|  | 

### Return type

[**BusinessExchangeRate**](BusinessExchangeRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Business Exchange Rate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

