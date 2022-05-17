# sage.PurchaseCreditNotesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_purchase_credit_notes_key**](PurchaseCreditNotesApi.md#delete_purchase_credit_notes_key) | **DELETE** /purchase_credit_notes/{key} | Deletes a Purchase Credit Note
[**get_purchase_credit_notes**](PurchaseCreditNotesApi.md#get_purchase_credit_notes) | **GET** /purchase_credit_notes | Returns all Purchase Credit Notes
[**get_purchase_credit_notes_key**](PurchaseCreditNotesApi.md#get_purchase_credit_notes_key) | **GET** /purchase_credit_notes/{key} | Returns a Purchase Credit Note
[**post_purchase_credit_notes**](PurchaseCreditNotesApi.md#post_purchase_credit_notes) | **POST** /purchase_credit_notes | Creates a Purchase Credit Note
[**post_purchase_credit_notes_key_release**](PurchaseCreditNotesApi.md#post_purchase_credit_notes_key_release) | **POST** /purchase_credit_notes/{key}/release | Releases a Purchase Credit Note
[**put_purchase_credit_notes_key**](PurchaseCreditNotesApi.md#put_purchase_credit_notes_key) | **PUT** /purchase_credit_notes/{key} | Updates a Purchase Credit Note


# **delete_purchase_credit_notes_key**
> delete_purchase_credit_notes_key(key)

Deletes a Purchase Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access

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
    api_instance = sage.PurchaseCreditNotesApi(api_client)
    key = 'key_example' # str | The Purchase Credit Note Key.

    try:
        # Deletes a Purchase Credit Note
        api_instance.delete_purchase_credit_notes_key(key)
    except ApiException as e:
        print("Exception when calling PurchaseCreditNotesApi->delete_purchase_credit_notes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Credit Note Key. | 

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
**204** | Deletes a Purchase Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_credit_notes**
> list[PurchaseCreditNote] get_purchase_credit_notes(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Purchase Credit Notes

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Standard: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.PurchaseCreditNotesApi(api_client)
    show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
search = 'search_example' # str | Use this to filter by the credit note reference or contact name. (optional)
contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
status_id = 'status_id_example' # str | Use this to filter by status id (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Purchase Credit Notes dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Purchase Credit Notes dates (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Purchase Credit Notes changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Purchase Credit Notes deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
has_attachments = True # bool | Use this to filter Purchase Credit Notes by whether they have attachments or not (optional)
items_per_page = 20 # int | Returns the given number of Purchase Credit Notes per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Purchase Credit Notes (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Purchase Credit Notes (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Purchase Credit Notes
        api_response = api_instance.get_purchase_credit_notes(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseCreditNotesApi->get_purchase_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **search** | **str**| Use this to filter by the credit note reference or contact name. | [optional] 
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **status_id** | **str**| Use this to filter by status id | [optional] 
 **from_date** | **datetime**| Use this to filter by Purchase Credit Notes dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Purchase Credit Notes dates | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Purchase Credit Notes changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Purchase Credit Notes deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **has_attachments** | **bool**| Use this to filter Purchase Credit Notes by whether they have attachments or not | [optional] 
 **items_per_page** | **int**| Returns the given number of Purchase Credit Notes per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Purchase Credit Notes | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Purchase Credit Notes (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[PurchaseCreditNote]**](PurchaseCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Purchase Credit Notes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_credit_notes_key**
> PurchaseCreditNote get_purchase_credit_notes_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, attributes=attributes)

Returns a Purchase Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Standard: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.PurchaseCreditNotesApi(api_client)
    key = 'key_example' # str | The Purchase Credit Note Key.
show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Purchase Credit Note (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Purchase Credit Note (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Purchase Credit Note
        api_response = api_instance.get_purchase_credit_notes_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseCreditNotesApi->get_purchase_credit_notes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Credit Note Key. | 
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Purchase Credit Note (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Purchase Credit Note (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**PurchaseCreditNote**](PurchaseCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Purchase Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_purchase_credit_notes**
> PurchaseCreditNote post_purchase_credit_notes(purchase_credit_notes)

Creates a Purchase Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Restricted Access

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
    api_instance = sage.PurchaseCreditNotesApi(api_client)
    purchase_credit_notes = sage.PostPurchaseCreditNotes() # PostPurchaseCreditNotes | 

    try:
        # Creates a Purchase Credit Note
        api_response = api_instance.post_purchase_credit_notes(purchase_credit_notes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseCreditNotesApi->post_purchase_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_credit_notes** | [**PostPurchaseCreditNotes**](PostPurchaseCreditNotes.md)|  | 

### Return type

[**PurchaseCreditNote**](PurchaseCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Purchase Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_purchase_credit_notes_key_release**
> PurchaseCreditNote post_purchase_credit_notes_key_release(key)

Releases a Purchase Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Restricted Access

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
    api_instance = sage.PurchaseCreditNotesApi(api_client)
    key = 'key_example' # str | The Purchase Credit Note Key.

    try:
        # Releases a Purchase Credit Note
        api_response = api_instance.post_purchase_credit_notes_key_release(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseCreditNotesApi->post_purchase_credit_notes_key_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Credit Note Key. | 

### Return type

[**PurchaseCreditNote**](PurchaseCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Releases a Purchase Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_purchase_credit_notes_key**
> PurchaseCreditNote put_purchase_credit_notes_key(key, purchase_credit_notes)

Updates a Purchase Credit Note

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Restricted Access

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
    api_instance = sage.PurchaseCreditNotesApi(api_client)
    key = 'key_example' # str | The Purchase Credit Note Key.
purchase_credit_notes = sage.PutPurchaseCreditNotes() # PutPurchaseCreditNotes | 

    try:
        # Updates a Purchase Credit Note
        api_response = api_instance.put_purchase_credit_notes_key(key, purchase_credit_notes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseCreditNotesApi->put_purchase_credit_notes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Credit Note Key. | 
 **purchase_credit_notes** | [**PutPurchaseCreditNotes**](PutPurchaseCreditNotes.md)|  | 

### Return type

[**PurchaseCreditNote**](PurchaseCreditNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Purchase Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

