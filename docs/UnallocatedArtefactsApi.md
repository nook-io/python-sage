# sage.UnallocatedArtefactsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_unallocated_artefacts**](UnallocatedArtefactsApi.md#get_unallocated_artefacts) | **GET** /unallocated_artefacts | Returns all Unallocated Artefacts
[**get_unallocated_artefacts_key**](UnallocatedArtefactsApi.md#get_unallocated_artefacts_key) | **GET** /unallocated_artefacts/{key} | Returns a Unallocated Artefact


# **get_unallocated_artefacts**
> list[UnallocatedArtefact] get_unallocated_artefacts(contact_id=contact_id, search=search, attributes=attributes, items_per_page=items_per_page, page=page)

Returns all Unallocated Artefacts

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.UnallocatedArtefactsApi(api_client)
    contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
search = 'search_example' # str | Use this to filter by the contact identifier. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Base Artefacts (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
items_per_page = 20 # int | Returns the given number of Base Artefacts per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Base Artefacts (optional) (default to 1)

    try:
        # Returns all Unallocated Artefacts
        api_response = api_instance.get_unallocated_artefacts(contact_id=contact_id, search=search, attributes=attributes, items_per_page=items_per_page, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UnallocatedArtefactsApi->get_unallocated_artefacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **search** | **str**| Use this to filter by the contact identifier. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Base Artefacts (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **items_per_page** | **int**| Returns the given number of Base Artefacts per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Base Artefacts | [optional] [default to 1]

### Return type

[**list[UnallocatedArtefact]**](UnallocatedArtefact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Unallocated Artefacts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unallocated_artefacts_key**
> UnallocatedArtefact get_unallocated_artefacts_key(key, attributes=attributes)

Returns a Unallocated Artefact

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.UnallocatedArtefactsApi(api_client)
    key = 'key_example' # str | The Unallocated Artefact Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Base Artefact (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Unallocated Artefact
        api_response = api_instance.get_unallocated_artefacts_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UnallocatedArtefactsApi->get_unallocated_artefacts_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Unallocated Artefact Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Base Artefact (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**UnallocatedArtefact**](UnallocatedArtefact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Unallocated Artefact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

