# sage.SalesQuickEntriesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_quick_entries_key**](SalesQuickEntriesApi.md#delete_sales_quick_entries_key) | **DELETE** /sales_quick_entries/{key} | Deletes a Sales Quick Entry
[**get_sales_quick_entries**](SalesQuickEntriesApi.md#get_sales_quick_entries) | **GET** /sales_quick_entries | Returns all Sales Quick Entries
[**get_sales_quick_entries_key**](SalesQuickEntriesApi.md#get_sales_quick_entries_key) | **GET** /sales_quick_entries/{key} | Returns a Sales Quick Entry
[**post_sales_quick_entries**](SalesQuickEntriesApi.md#post_sales_quick_entries) | **POST** /sales_quick_entries | Creates a Sales Quick Entry
[**put_sales_quick_entries_key**](SalesQuickEntriesApi.md#put_sales_quick_entries_key) | **PUT** /sales_quick_entries/{key} | Updates a Sales Quick Entry


# **delete_sales_quick_entries_key**
> delete_sales_quick_entries_key(key)

Deletes a Sales Quick Entry

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access

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
    api_instance = sage.SalesQuickEntriesApi(api_client)
    key = 'key_example' # str | The Sales Quick Entry Key.

    try:
        # Deletes a Sales Quick Entry
        api_instance.delete_sales_quick_entries_key(key)
    except ApiException as e:
        print("Exception when calling SalesQuickEntriesApi->delete_sales_quick_entries_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Quick Entry Key. | 

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
**204** | Deletes a Sales Quick Entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_quick_entries**
> list[QuickEntry] get_sales_quick_entries(contact_id=contact_id, search=search, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, show_payments_allocations=show_payments_allocations, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Sales Quick Entries

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.SalesQuickEntriesApi(api_client)
    contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
search = 'search_example' # str | Use this to filter by the quick entry reference or contact name. (optional)
status_id = 'status_id_example' # str | Use this to filter by status id (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Batch Entries dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Batch Entries dates (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Sales Batch Entries changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Sales Batch Entries deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
has_attachments = True # bool | Use this to filter Sales Batch Entries by whether they have attachments or not (optional)
items_per_page = 20 # int | Returns the given number of Sales Batch Entries per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Sales Batch Entries (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Batch Entries (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Sales Quick Entries
        api_response = api_instance.get_sales_quick_entries(contact_id=contact_id, search=search, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, show_payments_allocations=show_payments_allocations, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesQuickEntriesApi->get_sales_quick_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **search** | **str**| Use this to filter by the quick entry reference or contact name. | [optional] 
 **status_id** | **str**| Use this to filter by status id | [optional] 
 **from_date** | **datetime**| Use this to filter by Sales Batch Entries dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Sales Batch Entries dates | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Sales Batch Entries changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Sales Batch Entries deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **has_attachments** | **bool**| Use this to filter Sales Batch Entries by whether they have attachments or not | [optional] 
 **items_per_page** | **int**| Returns the given number of Sales Batch Entries per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Sales Batch Entries | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Batch Entries (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[QuickEntry]**](QuickEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Sales Quick Entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_quick_entries_key**
> QuickEntry get_sales_quick_entries_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, attributes=attributes)

Returns a Sales Quick Entry

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.SalesQuickEntriesApi(api_client)
    key = 'key_example' # str | The Sales Quick Entry Key.
show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Sales Batch Entry (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Batch Entry (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Sales Quick Entry
        api_response = api_instance.get_sales_quick_entries_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesQuickEntriesApi->get_sales_quick_entries_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Quick Entry Key. | 
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Sales Batch Entry (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Batch Entry (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**QuickEntry**](QuickEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Sales Quick Entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_quick_entries**
> QuickEntry post_sales_quick_entries(sales_quick_entries)

Creates a Sales Quick Entry

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesQuickEntriesApi(api_client)
    sales_quick_entries = sage.PostSalesQuickEntries() # PostSalesQuickEntries | 

    try:
        # Creates a Sales Quick Entry
        api_response = api_instance.post_sales_quick_entries(sales_quick_entries)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesQuickEntriesApi->post_sales_quick_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_quick_entries** | [**PostSalesQuickEntries**](PostSalesQuickEntries.md)|  | 

### Return type

[**QuickEntry**](QuickEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Sales Quick Entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_quick_entries_key**
> QuickEntry put_sales_quick_entries_key(key, sales_quick_entries)

Updates a Sales Quick Entry

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesQuickEntriesApi(api_client)
    key = 'key_example' # str | The Sales Quick Entry Key.
sales_quick_entries = sage.PutSalesQuickEntries() # PutSalesQuickEntries | 

    try:
        # Updates a Sales Quick Entry
        api_response = api_instance.put_sales_quick_entries_key(key, sales_quick_entries)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesQuickEntriesApi->put_sales_quick_entries_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Quick Entry Key. | 
 **sales_quick_entries** | [**PutSalesQuickEntries**](PutSalesQuickEntries.md)|  | 

### Return type

[**QuickEntry**](QuickEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Sales Quick Entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

