# sage.TaxProfilesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tax_profiles**](TaxProfilesApi.md#get_tax_profiles) | **GET** /tax_profiles | Returns all Tax Profiles
[**get_tax_profiles_key**](TaxProfilesApi.md#get_tax_profiles_key) | **GET** /tax_profiles/{key} | Returns a Tax Profile
[**put_tax_profiles_key**](TaxProfilesApi.md#put_tax_profiles_key) | **PUT** /tax_profiles/{key} | Updates a Tax Profile


# **get_tax_profiles**
> list[TaxProfile] get_tax_profiles(updated_or_created_since=updated_or_created_since, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Tax Profiles

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access, Read Only

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
    api_instance = sage.TaxProfilesApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Tax Profiles changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
items_per_page = 20 # int | Returns the given number of Tax Profiles per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Tax Profiles (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Profiles (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Tax Profiles
        api_response = api_instance.get_tax_profiles(updated_or_created_since=updated_or_created_since, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxProfilesApi->get_tax_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Tax Profiles changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **items_per_page** | **int**| Returns the given number of Tax Profiles per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Tax Profiles | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Profiles (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[TaxProfile]**](TaxProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Tax Profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_profiles_key**
> TaxProfile get_tax_profiles_key(key, attributes=attributes)

Returns a Tax Profile

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access, Read Only

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
    api_instance = sage.TaxProfilesApi(api_client)
    key = 'key_example' # str | The Tax Profile Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Profile (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Tax Profile
        api_response = api_instance.get_tax_profiles_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxProfilesApi->get_tax_profiles_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Tax Profile Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Profile (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**TaxProfile**](TaxProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Tax Profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tax_profiles_key**
> TaxProfile put_tax_profiles_key(key, tax_profiles)

Updates a Tax Profile

### Endpoint Availability  * Accounting Plus: 🇨🇦 * Accounting Standard: 🇨🇦 * Accounting Start: 🇨🇦  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = sage.TaxProfilesApi(api_client)
    key = 'key_example' # str | The Tax Profile Key.
tax_profiles = sage.PutTaxProfiles() # PutTaxProfiles | 

    try:
        # Updates a Tax Profile
        api_response = api_instance.put_tax_profiles_key(key, tax_profiles)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxProfilesApi->put_tax_profiles_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Tax Profile Key. | 
 **tax_profiles** | [**PutTaxProfiles**](PutTaxProfiles.md)|  | 

### Return type

[**TaxProfile**](TaxProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Tax Profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

