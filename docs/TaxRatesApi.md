# sage.TaxRatesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tax_rates_key**](TaxRatesApi.md#delete_tax_rates_key) | **DELETE** /tax_rates/{key} | Deletes a Tax Rate (US only)
[**get_tax_rates**](TaxRatesApi.md#get_tax_rates) | **GET** /tax_rates | Returns all Tax Rates
[**get_tax_rates_key**](TaxRatesApi.md#get_tax_rates_key) | **GET** /tax_rates/{key} | Returns a Tax Rate
[**post_tax_rates**](TaxRatesApi.md#post_tax_rates) | **POST** /tax_rates | Creates a Tax Rate (US only)
[**put_tax_rates_key**](TaxRatesApi.md#put_tax_rates_key) | **PUT** /tax_rates/{key} | Updates a Tax Rate (US only)


# **delete_tax_rates_key**
> delete_tax_rates_key(key)

Deletes a Tax Rate (US only)

  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = sage.TaxRatesApi(api_client)
    key = 'key_example' # str | The Tax Rate key.

    try:
        # Deletes a Tax Rate (US only)
        api_instance.delete_tax_rates_key(key)
    except ApiException as e:
        print("Exception when calling TaxRatesApi->delete_tax_rates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Tax Rate key. | 

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
**204** | Deletes a Tax Rate (US only) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_rates**
> list[TaxRate] get_tax_rates(updated_or_created_since=updated_or_created_since, address_region_id=address_region_id, date=date, include_historical_data=include_historical_data, cis_only=cis_only, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Tax Rates

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Full Access, Restricted Access, Read Only * Area: `Purchases`: Full Access, Restricted Access, Read Only * Area: `Bank`: Full Access, Restricted Access, Read Only * Area: `Settings`: Full Access, Read Only

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
    api_instance = sage.TaxRatesApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Tax Rates changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
address_region_id = 'address_region_id_example' # str | Use this to filter by address region id (optional)
date = '2013-10-20' # date | Use this to return results on a specified date. (optional)
include_historical_data = True # bool | Use this to include historical data in the response (optional)
cis_only = True # bool | Use this to filter Tax Rates to CIS only records (optional)
items_per_page = 20 # int | Returns the given number of Tax Rates per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Tax Rates (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Rates (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Tax Rates
        api_response = api_instance.get_tax_rates(updated_or_created_since=updated_or_created_since, address_region_id=address_region_id, date=date, include_historical_data=include_historical_data, cis_only=cis_only, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxRatesApi->get_tax_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Tax Rates changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **address_region_id** | **str**| Use this to filter by address region id | [optional] 
 **date** | **date**| Use this to return results on a specified date. | [optional] 
 **include_historical_data** | **bool**| Use this to include historical data in the response | [optional] 
 **cis_only** | **bool**| Use this to filter Tax Rates to CIS only records | [optional] 
 **items_per_page** | **int**| Returns the given number of Tax Rates per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Tax Rates | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Rates (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[TaxRate]**](TaxRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Tax Rates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_rates_key**
> TaxRate get_tax_rates_key(key, date=date, attributes=attributes)

Returns a Tax Rate

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Full Access, Restricted Access, Read Only * Area: `Purchases`: Full Access, Restricted Access, Read Only * Area: `Bank`: Full Access, Restricted Access, Read Only * Area: `Settings`: Full Access, Read Only

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
    api_instance = sage.TaxRatesApi(api_client)
    key = 'key_example' # str | The Tax Rate Key.
date = '2013-10-20' # date | Use this to show the tax rate percentage on the given date (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Rate (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Tax Rate
        api_response = api_instance.get_tax_rates_key(key, date=date, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxRatesApi->get_tax_rates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Tax Rate Key. | 
 **date** | **date**| Use this to show the tax rate percentage on the given date | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Rate (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**TaxRate**](TaxRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Tax Rate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tax_rates**
> TaxRate post_tax_rates(tax_rates)

Creates a Tax Rate (US only)

  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = sage.TaxRatesApi(api_client)
    tax_rates = sage.PostTaxRates() # PostTaxRates | 

    try:
        # Creates a Tax Rate (US only)
        api_response = api_instance.post_tax_rates(tax_rates)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxRatesApi->post_tax_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rates** | [**PostTaxRates**](PostTaxRates.md)|  | 

### Return type

[**TaxRate**](TaxRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Tax Rate (US only) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tax_rates_key**
> TaxRate put_tax_rates_key(key, tax_rates)

Updates a Tax Rate (US only)

  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = sage.TaxRatesApi(api_client)
    key = 'key_example' # str | The Tax Rate key.
tax_rates = sage.PutTaxRates() # PutTaxRates | 

    try:
        # Updates a Tax Rate (US only)
        api_response = api_instance.put_tax_rates_key(key, tax_rates)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxRatesApi->put_tax_rates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Tax Rate key. | 
 **tax_rates** | [**PutTaxRates**](PutTaxRates.md)|  | 

### Return type

[**TaxRate**](TaxRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Tax Rate (US only) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

