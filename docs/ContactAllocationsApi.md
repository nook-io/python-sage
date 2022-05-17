# sage.ContactAllocationsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_contact_allocations_key**](ContactAllocationsApi.md#delete_contact_allocations_key) | **DELETE** /contact_allocations/{key} | Deletes a Contact Allocation
[**get_contact_allocations**](ContactAllocationsApi.md#get_contact_allocations) | **GET** /contact_allocations | Returns all Contact Allocations
[**get_contact_allocations_key**](ContactAllocationsApi.md#get_contact_allocations_key) | **GET** /contact_allocations/{key} | Returns a Contact Allocation
[**post_contact_allocations**](ContactAllocationsApi.md#post_contact_allocations) | **POST** /contact_allocations | Creates a Contact Allocation
[**put_contact_allocations_key**](ContactAllocationsApi.md#put_contact_allocations_key) | **PUT** /contact_allocations/{key} | Updates a Contact Allocation


# **delete_contact_allocations_key**
> delete_contact_allocations_key(key)

Deletes a Contact Allocation

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, and `Contacts`: Full Access

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
    api_instance = sage.ContactAllocationsApi(api_client)
    key = 'key_example' # str | The Contact Allocation Key.

    try:
        # Deletes a Contact Allocation
        api_instance.delete_contact_allocations_key(key)
    except ApiException as e:
        print("Exception when calling ContactAllocationsApi->delete_contact_allocations_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Allocation Key. | 

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
**204** | Deletes a Contact Allocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_allocations**
> list[ContactAllocation] get_contact_allocations(contact_id=contact_id, transaction_type_id=transaction_type_id, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Contact Allocations

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, and `Contacts`: Full Access

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
    api_instance = sage.ContactAllocationsApi(api_client)
    contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
transaction_type_id = 'transaction_type_id_example' # str | Use this to filter by transaction type id (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Allocations changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Allocations deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
items_per_page = 20 # int | Returns the given number of Allocations per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Allocations (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Allocations (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Contact Allocations
        api_response = api_instance.get_contact_allocations(contact_id=contact_id, transaction_type_id=transaction_type_id, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactAllocationsApi->get_contact_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **transaction_type_id** | **str**| Use this to filter by transaction type id | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Allocations changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Allocations deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **items_per_page** | **int**| Returns the given number of Allocations per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Allocations | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Allocations (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[ContactAllocation]**](ContactAllocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Contact Allocations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_allocations_key**
> ContactAllocation get_contact_allocations_key(key, attributes=attributes)

Returns a Contact Allocation

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, and `Contacts`: Full Access

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
    api_instance = sage.ContactAllocationsApi(api_client)
    key = 'key_example' # str | The Contact Allocation Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Allocation (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Contact Allocation
        api_response = api_instance.get_contact_allocations_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactAllocationsApi->get_contact_allocations_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Allocation Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Allocation (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**ContactAllocation**](ContactAllocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Contact Allocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_contact_allocations**
> ContactAllocation post_contact_allocations(contact_allocations)

Creates a Contact Allocation

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, and `Contacts`: Full Access

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
    api_instance = sage.ContactAllocationsApi(api_client)
    contact_allocations = sage.PostContactAllocations() # PostContactAllocations | 

    try:
        # Creates a Contact Allocation
        api_response = api_instance.post_contact_allocations(contact_allocations)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactAllocationsApi->post_contact_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_allocations** | [**PostContactAllocations**](PostContactAllocations.md)|  | 

### Return type

[**ContactAllocation**](ContactAllocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Contact Allocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_contact_allocations_key**
> ContactAllocation put_contact_allocations_key(key, contact_allocations)

Updates a Contact Allocation

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, and `Contacts`: Full Access

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
    api_instance = sage.ContactAllocationsApi(api_client)
    key = 'key_example' # str | The Contact Allocation Key.
contact_allocations = sage.PutContactAllocations() # PutContactAllocations | 

    try:
        # Updates a Contact Allocation
        api_response = api_instance.put_contact_allocations_key(key, contact_allocations)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactAllocationsApi->put_contact_allocations_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Allocation Key. | 
 **contact_allocations** | [**PutContactAllocations**](PutContactAllocations.md)|  | 

### Return type

[**ContactAllocation**](ContactAllocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Contact Allocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

