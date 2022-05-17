# sage.PurchaseInvoicesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_purchase_invoices_key**](PurchaseInvoicesApi.md#delete_purchase_invoices_key) | **DELETE** /purchase_invoices/{key} | Deletes a Purchase Invoice
[**get_purchase_invoices**](PurchaseInvoicesApi.md#get_purchase_invoices) | **GET** /purchase_invoices | Returns all Purchase Invoices
[**get_purchase_invoices_key**](PurchaseInvoicesApi.md#get_purchase_invoices_key) | **GET** /purchase_invoices/{key} | Returns a Purchase Invoice
[**post_purchase_invoices**](PurchaseInvoicesApi.md#post_purchase_invoices) | **POST** /purchase_invoices | Creates a Purchase Invoice
[**post_purchase_invoices_key_release**](PurchaseInvoicesApi.md#post_purchase_invoices_key_release) | **POST** /purchase_invoices/{key}/release | Releases a Purchase Invoice
[**put_purchase_invoices_key**](PurchaseInvoicesApi.md#put_purchase_invoices_key) | **PUT** /purchase_invoices/{key} | Updates a Purchase Invoice


# **delete_purchase_invoices_key**
> delete_purchase_invoices_key(key)

Deletes a Purchase Invoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access

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
    api_instance = sage.PurchaseInvoicesApi(api_client)
    key = 'key_example' # str | The Purchase Invoice Key.

    try:
        # Deletes a Purchase Invoice
        api_instance.delete_purchase_invoices_key(key)
    except ApiException as e:
        print("Exception when calling PurchaseInvoicesApi->delete_purchase_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Invoice Key. | 

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
**204** | Deletes a Purchase Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_invoices**
> list[PurchaseInvoice] get_purchase_invoices(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Purchase Invoices

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.PurchaseInvoicesApi(api_client)
    show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
search = 'search_example' # str | Use this to filter by the invoice reference or contact name. (optional)
contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
status_id = 'status_id_example' # str | Use this to filter by status id (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Purchase Invoices dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Purchase Invoices dates (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Purchase Invoices changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Purchase Invoices deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
has_attachments = True # bool | Use this to filter Purchase Invoices by whether they have attachments or not (optional)
items_per_page = 20 # int | Returns the given number of Purchase Invoices per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Purchase Invoices (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Purchase Invoices (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date, due_date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Purchase Invoices
        api_response = api_instance.get_purchase_invoices(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseInvoicesApi->get_purchase_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **search** | **str**| Use this to filter by the invoice reference or contact name. | [optional] 
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **status_id** | **str**| Use this to filter by status id | [optional] 
 **from_date** | **datetime**| Use this to filter by Purchase Invoices dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Purchase Invoices dates | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Purchase Invoices changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Purchase Invoices deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **has_attachments** | **bool**| Use this to filter Purchase Invoices by whether they have attachments or not | [optional] 
 **items_per_page** | **int**| Returns the given number of Purchase Invoices per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Purchase Invoices | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Purchase Invoices (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date, due_date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[PurchaseInvoice]**](PurchaseInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Purchase Invoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_invoices_key**
> PurchaseInvoice get_purchase_invoices_key(key, show_payments_allocations=show_payments_allocations, show_corrections=show_corrections, nested_attributes=nested_attributes, attributes=attributes)

Returns a Purchase Invoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.PurchaseInvoicesApi(api_client)
    key = 'key_example' # str | The Purchase Invoice Key.
show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
show_corrections = True # bool | Use this to show the artefact's associated corrections (optional)
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Purchase Invoice (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Purchase Invoice (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Purchase Invoice
        api_response = api_instance.get_purchase_invoices_key(key, show_payments_allocations=show_payments_allocations, show_corrections=show_corrections, nested_attributes=nested_attributes, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseInvoicesApi->get_purchase_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Invoice Key. | 
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **show_corrections** | **bool**| Use this to show the artefact&#39;s associated corrections | [optional] 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Purchase Invoice (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Purchase Invoice (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Purchase Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_purchase_invoices**
> PurchaseInvoice post_purchase_invoices(purchase_invoices)

Creates a Purchase Invoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Restricted Access

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
    api_instance = sage.PurchaseInvoicesApi(api_client)
    purchase_invoices = sage.PostPurchaseInvoices() # PostPurchaseInvoices | 

    try:
        # Creates a Purchase Invoice
        api_response = api_instance.post_purchase_invoices(purchase_invoices)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseInvoicesApi->post_purchase_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_invoices** | [**PostPurchaseInvoices**](PostPurchaseInvoices.md)|  | 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Purchase Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_purchase_invoices_key_release**
> PurchaseInvoice post_purchase_invoices_key_release(key)

Releases a Purchase Invoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Restricted Access

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
    api_instance = sage.PurchaseInvoicesApi(api_client)
    key = 'key_example' # str | The Purchase Invoice Key.

    try:
        # Releases a Purchase Invoice
        api_response = api_instance.post_purchase_invoices_key_release(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseInvoicesApi->post_purchase_invoices_key_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Invoice Key. | 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Releases a Purchase Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_purchase_invoices_key**
> PurchaseInvoice put_purchase_invoices_key(key, purchase_invoices)

Updates a Purchase Invoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Restricted Access

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
    api_instance = sage.PurchaseInvoicesApi(api_client)
    key = 'key_example' # str | The Purchase Invoice Key.
purchase_invoices = sage.PutPurchaseInvoices() # PutPurchaseInvoices | 

    try:
        # Updates a Purchase Invoice
        api_response = api_instance.put_purchase_invoices_key(key, purchase_invoices)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseInvoicesApi->put_purchase_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Invoice Key. | 
 **purchase_invoices** | [**PutPurchaseInvoices**](PutPurchaseInvoices.md)|  | 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Purchase Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

