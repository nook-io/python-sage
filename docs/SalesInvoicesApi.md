# sage.SalesInvoicesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_invoices_key**](SalesInvoicesApi.md#delete_sales_invoices_key) | **DELETE** /sales_invoices/{key} | Voids a Sales Invoice
[**get_sales_invoices**](SalesInvoicesApi.md#get_sales_invoices) | **GET** /sales_invoices | Returns all Sales Invoices
[**get_sales_invoices_key**](SalesInvoicesApi.md#get_sales_invoices_key) | **GET** /sales_invoices/{key} | Returns a Sales Invoice
[**post_sales_invoices**](SalesInvoicesApi.md#post_sales_invoices) | **POST** /sales_invoices | Creates a Sales Invoice
[**post_sales_invoices_key_release**](SalesInvoicesApi.md#post_sales_invoices_key_release) | **POST** /sales_invoices/{key}/release | Releases a Sales Invoice
[**put_sales_invoices_key**](SalesInvoicesApi.md#put_sales_invoices_key) | **PUT** /sales_invoices/{key} | Updates a Sales Invoice


# **delete_sales_invoices_key**
> SalesInvoice delete_sales_invoices_key(key, void_reason=void_reason)

Voids a Sales Invoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access

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
    api_instance = sage.SalesInvoicesApi(api_client)
    key = 'key_example' # str | The Sales Invoice Key.
void_reason = 'void_reason_example' # str | The reason the Sales Invoice is being voided (required unless status is DRAFT). (optional)

    try:
        # Voids a Sales Invoice
        api_response = api_instance.delete_sales_invoices_key(key, void_reason=void_reason)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesInvoicesApi->delete_sales_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Invoice Key. | 
 **void_reason** | **str**| The reason the Sales Invoice is being voided (required unless status is DRAFT). | [optional] 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Voids a Sales Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_invoices**
> list[SalesInvoice] get_sales_invoices(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Sales Invoices

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
    api_instance = sage.SalesInvoicesApi(api_client)
    show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
search = 'search_example' # str | Use this to filter by the invoice reference or contact name. (optional)
contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
status_id = 'status_id_example' # str | Use this to filter by status id (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Invoices dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Invoices dates (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Sales Invoices changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Sales Invoices deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
has_attachments = True # bool | Use this to filter Sales Invoices by whether they have attachments or not (optional)
items_per_page = 20 # int | Returns the given number of Sales Invoices per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Sales Invoices (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Invoices (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date, due_date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Sales Invoices
        api_response = api_instance.get_sales_invoices(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesInvoicesApi->get_sales_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **search** | **str**| Use this to filter by the invoice reference or contact name. | [optional] 
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **status_id** | **str**| Use this to filter by status id | [optional] 
 **from_date** | **datetime**| Use this to filter by Sales Invoices dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Sales Invoices dates | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Sales Invoices changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Sales Invoices deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **has_attachments** | **bool**| Use this to filter Sales Invoices by whether they have attachments or not | [optional] 
 **items_per_page** | **int**| Returns the given number of Sales Invoices per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Sales Invoices | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Invoices (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date, due_date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[SalesInvoice]**](SalesInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Sales Invoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_invoices_key**
> SalesInvoice get_sales_invoices_key(key, show_payments_allocations=show_payments_allocations, show_corrections=show_corrections, nested_attributes=nested_attributes, mark_as_sent=mark_as_sent, show_recurring_invoice=show_recurring_invoice, attributes=attributes)

Returns a Sales Invoice

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
    api_instance = sage.SalesInvoicesApi(api_client)
    key = 'key_example' # str | The Sales Invoice Key.
show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
show_corrections = True # bool | Use this to show the artefact's associated corrections (optional)
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Sales Invoice (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
mark_as_sent = True # bool | Use this to mark/not mark the artefact as sent. Defaulted to 'true'. (optional)
show_recurring_invoice = True # bool | Use this to show the artefact's associated recurring invoice template if present (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Invoice (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Sales Invoice
        api_response = api_instance.get_sales_invoices_key(key, show_payments_allocations=show_payments_allocations, show_corrections=show_corrections, nested_attributes=nested_attributes, mark_as_sent=mark_as_sent, show_recurring_invoice=show_recurring_invoice, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesInvoicesApi->get_sales_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Invoice Key. | 
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **show_corrections** | **bool**| Use this to show the artefact&#39;s associated corrections | [optional] 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Sales Invoice (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **mark_as_sent** | **bool**| Use this to mark/not mark the artefact as sent. Defaulted to &#39;true&#39;. | [optional] 
 **show_recurring_invoice** | **bool**| Use this to show the artefact&#39;s associated recurring invoice template if present | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Invoice (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Sales Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_invoices**
> SalesInvoice post_sales_invoices(sales_invoices)

Creates a Sales Invoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesInvoicesApi(api_client)
    sales_invoices = sage.PostSalesInvoices() # PostSalesInvoices | 

    try:
        # Creates a Sales Invoice
        api_response = api_instance.post_sales_invoices(sales_invoices)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesInvoicesApi->post_sales_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_invoices** | [**PostSalesInvoices**](PostSalesInvoices.md)|  | 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Sales Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_invoices_key_release**
> SalesInvoice post_sales_invoices_key_release(key)

Releases a Sales Invoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesInvoicesApi(api_client)
    key = 'key_example' # str | The Sales Invoice Key.

    try:
        # Releases a Sales Invoice
        api_response = api_instance.post_sales_invoices_key_release(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesInvoicesApi->post_sales_invoices_key_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Invoice Key. | 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Releases a Sales Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_invoices_key**
> SalesInvoice put_sales_invoices_key(key, sales_invoices)

Updates a Sales Invoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesInvoicesApi(api_client)
    key = 'key_example' # str | The Sales Invoice Key.
sales_invoices = sage.PutSalesInvoices() # PutSalesInvoices | 

    try:
        # Updates a Sales Invoice
        api_response = api_instance.put_sales_invoices_key(key, sales_invoices)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesInvoicesApi->put_sales_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Invoice Key. | 
 **sales_invoices** | [**PutSalesInvoices**](PutSalesInvoices.md)|  | 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Sales Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

