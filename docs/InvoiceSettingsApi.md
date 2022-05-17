# sage.InvoiceSettingsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_settings**](InvoiceSettingsApi.md#get_invoice_settings) | **GET** /invoice_settings | Returns all Invoice Settings
[**put_invoice_settings**](InvoiceSettingsApi.md#put_invoice_settings) | **PUT** /invoice_settings | Updates a Invoice Settings


# **get_invoice_settings**
> InvoiceSettings get_invoice_settings()

Returns all Invoice Settings

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access, Read Only

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
    api_instance = sage.InvoiceSettingsApi(api_client)
    
    try:
        # Returns all Invoice Settings
        api_response = api_instance.get_invoice_settings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvoiceSettingsApi->get_invoice_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InvoiceSettings**](InvoiceSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Invoice Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_invoice_settings**
> InvoiceSettings put_invoice_settings(invoice_settings)

Updates a Invoice Settings

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = sage.InvoiceSettingsApi(api_client)
    invoice_settings = sage.PutInvoiceSettings() # PutInvoiceSettings | 

    try:
        # Updates a Invoice Settings
        api_response = api_instance.put_invoice_settings(invoice_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvoiceSettingsApi->put_invoice_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_settings** | [**PutInvoiceSettings**](PutInvoiceSettings.md)|  | 

### Return type

[**InvoiceSettings**](InvoiceSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Invoice Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

