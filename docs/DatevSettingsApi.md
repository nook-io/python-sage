# sage.DatevSettingsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_datev_settings**](DatevSettingsApi.md#get_datev_settings) | **GET** /datev_settings | Returns all Datev Settings
[**put_datev_settings**](DatevSettingsApi.md#put_datev_settings) | **PUT** /datev_settings | Updates a Datev Settings


# **get_datev_settings**
> DatevSettings get_datev_settings()

Returns all Datev Settings

### Endpoint Availability  * Accounting Plus: 🇩🇪 * Accounting Standard: 🇩🇪 * Accounting Start: 🇩🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access, Read Only

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
    api_instance = sage.DatevSettingsApi(api_client)
    
    try:
        # Returns all Datev Settings
        api_response = api_instance.get_datev_settings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatevSettingsApi->get_datev_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DatevSettings**](DatevSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Datev Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_datev_settings**
> DatevSettings put_datev_settings(datev_settings)

Updates a Datev Settings

### Endpoint Availability  * Accounting Plus: 🇩🇪 * Accounting Standard: 🇩🇪 * Accounting Start: 🇩🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access

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
    api_instance = sage.DatevSettingsApi(api_client)
    datev_settings = sage.PutDatevSettings() # PutDatevSettings | 

    try:
        # Updates a Datev Settings
        api_response = api_instance.put_datev_settings(datev_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatevSettingsApi->put_datev_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datev_settings** | [**PutDatevSettings**](PutDatevSettings.md)|  | 

### Return type

[**DatevSettings**](DatevSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Datev Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

