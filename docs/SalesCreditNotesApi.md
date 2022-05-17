# sage.SalesCreditNotesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_credit_notes_key**](SalesCreditNotesApi.md#delete_sales_credit_notes_key) | **DELETE** /sales_credit_notes/{key} | Voids a Sales Credit Note
[**get_sales_credit_notes**](SalesCreditNotesApi.md#get_sales_credit_notes) | **GET** /sales_credit_notes | Returns all Sales Credit Notes
[**get_sales_credit_notes_key**](SalesCreditNotesApi.md#get_sales_credit_notes_key) | **GET** /sales_credit_notes/{key} | Returns a Sales Credit Note
[**post_sales_credit_notes**](SalesCreditNotesApi.md#post_sales_credit_notes) | **POST** /sales_credit_notes | Creates a Sales Credit Note
[**post_sales_credit_notes_key_release**](SalesCreditNotesApi.md#post_sales_credit_notes_key_release) | **POST** /sales_credit_notes/{key}/release | Releases a Sales Credit Note
[**put_sales_credit_notes_key**](SalesCreditNotesApi.md#put_sales_credit_notes_key) | **PUT** /sales_credit_notes/{key} | Updates a Sales Credit Note


# **delete_sales_credit_notes_key**
> SalesCreditNote delete_sales_credit_notes_key(key, void_reason=void_reason)

Voids a Sales Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access

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
    api_instance = sage.SalesCreditNotesApi(api_client)
    key = 'key_example' # str | The Sales Credit Note Key.
void_reason = 'void_reason_example' # str | The reason the Sales Credit Note is being voided (required unless status is DRAFT). (optional)

    try:
        # Voids a Sales Credit Note
        api_response = api_instance.delete_sales_credit_notes_key(key, void_reason=void_reason)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCreditNotesApi->delete_sales_credit_notes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Credit Note Key. | 
 **void_reason** | **str**| The reason the Sales Credit Note is being voided (required unless status is DRAFT). | [optional] 

### Return type

[**SalesCreditNote**](SalesCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Voids a Sales Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_credit_notes**
> list[SalesCreditNote] get_sales_credit_notes(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Sales Credit Notes

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Standard: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.SalesCreditNotesApi(api_client)
    show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
search = 'search_example' # str | Use this to filter by the credit note reference or contact name. (optional)
contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
status_id = 'status_id_example' # str | Use this to filter by status id (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Credit Notes dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Credit Notes dates (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Sales Credit Notes changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Sales Credit Notes deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
has_attachments = True # bool | Use this to filter Sales Credit Notes by whether they have attachments or not (optional)
items_per_page = 20 # int | Returns the given number of Sales Credit Notes per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Sales Credit Notes (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Credit Notes (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Sales Credit Notes
        api_response = api_instance.get_sales_credit_notes(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCreditNotesApi->get_sales_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **search** | **str**| Use this to filter by the credit note reference or contact name. | [optional] 
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **status_id** | **str**| Use this to filter by status id | [optional] 
 **from_date** | **datetime**| Use this to filter by Sales Credit Notes dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Sales Credit Notes dates | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Sales Credit Notes changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Sales Credit Notes deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **has_attachments** | **bool**| Use this to filter Sales Credit Notes by whether they have attachments or not | [optional] 
 **items_per_page** | **int**| Returns the given number of Sales Credit Notes per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Sales Credit Notes | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Credit Notes (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[SalesCreditNote]**](SalesCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Sales Credit Notes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_credit_notes_key**
> SalesCreditNote get_sales_credit_notes_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, mark_as_sent=mark_as_sent, attributes=attributes)

Returns a Sales Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Standard: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.SalesCreditNotesApi(api_client)
    key = 'key_example' # str | The Sales Credit Note Key.
show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Sales Credit Note (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
mark_as_sent = True # bool | Use this to mark/not mark the artefact as sent. Defaulted to 'true'. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Credit Note (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Sales Credit Note
        api_response = api_instance.get_sales_credit_notes_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, mark_as_sent=mark_as_sent, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCreditNotesApi->get_sales_credit_notes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Credit Note Key. | 
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Sales Credit Note (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **mark_as_sent** | **bool**| Use this to mark/not mark the artefact as sent. Defaulted to &#39;true&#39;. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Credit Note (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**SalesCreditNote**](SalesCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Sales Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_credit_notes**
> SalesCreditNote post_sales_credit_notes(sales_credit_notes)

Creates a Sales Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesCreditNotesApi(api_client)
    sales_credit_notes = sage.PostSalesCreditNotes() # PostSalesCreditNotes | 

    try:
        # Creates a Sales Credit Note
        api_response = api_instance.post_sales_credit_notes(sales_credit_notes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCreditNotesApi->post_sales_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_credit_notes** | [**PostSalesCreditNotes**](PostSalesCreditNotes.md)|  | 

### Return type

[**SalesCreditNote**](SalesCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Sales Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_credit_notes_key_release**
> SalesCreditNote post_sales_credit_notes_key_release(key)

Releases a Sales Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesCreditNotesApi(api_client)
    key = 'key_example' # str | The Sales Credit Note Key.

    try:
        # Releases a Sales Credit Note
        api_response = api_instance.post_sales_credit_notes_key_release(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCreditNotesApi->post_sales_credit_notes_key_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Credit Note Key. | 

### Return type

[**SalesCreditNote**](SalesCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Releases a Sales Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_credit_notes_key**
> SalesCreditNote put_sales_credit_notes_key(key, sales_credit_notes)

Updates a Sales Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesCreditNotesApi(api_client)
    key = 'key_example' # str | The Sales Credit Note Key.
sales_credit_notes = sage.PutSalesCreditNotes() # PutSalesCreditNotes | 

    try:
        # Updates a Sales Credit Note
        api_response = api_instance.put_sales_credit_notes_key(key, sales_credit_notes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCreditNotesApi->put_sales_credit_notes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Credit Note Key. | 
 **sales_credit_notes** | [**PutSalesCreditNotes**](PutSalesCreditNotes.md)|  | 

### Return type

[**SalesCreditNote**](SalesCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Sales Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

