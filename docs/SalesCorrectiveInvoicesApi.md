# sage.SalesCorrectiveInvoicesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_corrective_invoices_key**](SalesCorrectiveInvoicesApi.md#delete_sales_corrective_invoices_key) | **DELETE** /sales_corrective_invoices/{key} | Voids a Sales Corrective Invoice
[**get_sales_corrective_invoices**](SalesCorrectiveInvoicesApi.md#get_sales_corrective_invoices) | **GET** /sales_corrective_invoices | Returns all Sales Corrective Invoices
[**get_sales_corrective_invoices_key**](SalesCorrectiveInvoicesApi.md#get_sales_corrective_invoices_key) | **GET** /sales_corrective_invoices/{key} | Returns a Sales Corrective Invoice
[**post_sales_corrective_invoices**](SalesCorrectiveInvoicesApi.md#post_sales_corrective_invoices) | **POST** /sales_corrective_invoices | Creates a Sales Corrective Invoice
[**put_sales_corrective_invoices_key**](SalesCorrectiveInvoicesApi.md#put_sales_corrective_invoices_key) | **PUT** /sales_corrective_invoices/{key} | Updates a Sales Corrective Invoice


# **delete_sales_corrective_invoices_key**
> SalesCorrectiveInvoice delete_sales_corrective_invoices_key(key, void_reason=void_reason)

Voids a Sales Corrective Invoice

### Endpoint Availability  * Accounting Plus: 🇪🇸 * Accounting Standard: 🇪🇸 * Accounting Start: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access

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
    api_instance = sage.SalesCorrectiveInvoicesApi(api_client)
    key = 'key_example' # str | The Sales Corrective Invoice Key.
void_reason = 'void_reason_example' # str | The reason the Sales Corrective Invoice is being voided (required unless status is DRAFT). (optional)

    try:
        # Voids a Sales Corrective Invoice
        api_response = api_instance.delete_sales_corrective_invoices_key(key, void_reason=void_reason)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCorrectiveInvoicesApi->delete_sales_corrective_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Corrective Invoice Key. | 
 **void_reason** | **str**| The reason the Sales Corrective Invoice is being voided (required unless status is DRAFT). | [optional] 

### Return type

[**SalesCorrectiveInvoice**](SalesCorrectiveInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Voids a Sales Corrective Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_corrective_invoices**
> list[SalesCorrectiveInvoice] get_sales_corrective_invoices(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Sales Corrective Invoices

### Endpoint Availability  * Accounting Plus: 🇪🇸 * Accounting Standard: 🇪🇸 * Accounting Start: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.SalesCorrectiveInvoicesApi(api_client)
    show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
search = 'search_example' # str | Use this to filter by the invoice reference or contact name. (optional)
contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
status_id = 'status_id_example' # str | Use this to filter by status id (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Corrective Invoices dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Corrective Invoices dates (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Sales Corrective Invoices changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Sales Corrective Invoices deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
has_attachments = True # bool | Use this to filter Sales Corrective Invoices by whether they have attachments or not (optional)
items_per_page = 20 # int | Returns the given number of Sales Corrective Invoices per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Sales Corrective Invoices (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Corrective Invoices (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date, due_date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Sales Corrective Invoices
        api_response = api_instance.get_sales_corrective_invoices(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCorrectiveInvoicesApi->get_sales_corrective_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **search** | **str**| Use this to filter by the invoice reference or contact name. | [optional] 
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **status_id** | **str**| Use this to filter by status id | [optional] 
 **from_date** | **datetime**| Use this to filter by Sales Corrective Invoices dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Sales Corrective Invoices dates | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Sales Corrective Invoices changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Sales Corrective Invoices deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **has_attachments** | **bool**| Use this to filter Sales Corrective Invoices by whether they have attachments or not | [optional] 
 **items_per_page** | **int**| Returns the given number of Sales Corrective Invoices per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Sales Corrective Invoices | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Corrective Invoices (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date, due_date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[SalesCorrectiveInvoice]**](SalesCorrectiveInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Sales Corrective Invoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_corrective_invoices_key**
> SalesCorrectiveInvoice get_sales_corrective_invoices_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, mark_as_sent=mark_as_sent, attributes=attributes)

Returns a Sales Corrective Invoice

### Endpoint Availability  * Accounting Plus: 🇪🇸 * Accounting Standard: 🇪🇸 * Accounting Start: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.SalesCorrectiveInvoicesApi(api_client)
    key = 'key_example' # str | The Sales Corrective Invoice Key.
show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Sales Corrective Invoice (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
mark_as_sent = True # bool | Use this to mark/not mark the artefact as sent. Defaulted to 'true'. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Corrective Invoice (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Sales Corrective Invoice
        api_response = api_instance.get_sales_corrective_invoices_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, mark_as_sent=mark_as_sent, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCorrectiveInvoicesApi->get_sales_corrective_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Corrective Invoice Key. | 
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Sales Corrective Invoice (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **mark_as_sent** | **bool**| Use this to mark/not mark the artefact as sent. Defaulted to &#39;true&#39;. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Corrective Invoice (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**SalesCorrectiveInvoice**](SalesCorrectiveInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Sales Corrective Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_corrective_invoices**
> SalesCorrectiveInvoice post_sales_corrective_invoices(sales_corrective_invoices)

Creates a Sales Corrective Invoice

### Endpoint Availability  * Accounting Plus: 🇪🇸 * Accounting Standard: 🇪🇸 * Accounting Start: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesCorrectiveInvoicesApi(api_client)
    sales_corrective_invoices = sage.PostSalesCorrectiveInvoices() # PostSalesCorrectiveInvoices | 

    try:
        # Creates a Sales Corrective Invoice
        api_response = api_instance.post_sales_corrective_invoices(sales_corrective_invoices)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCorrectiveInvoicesApi->post_sales_corrective_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_corrective_invoices** | [**PostSalesCorrectiveInvoices**](PostSalesCorrectiveInvoices.md)|  | 

### Return type

[**SalesCorrectiveInvoice**](SalesCorrectiveInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Sales Corrective Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_corrective_invoices_key**
> SalesCorrectiveInvoice put_sales_corrective_invoices_key(key, sales_corrective_invoices)

Updates a Sales Corrective Invoice

### Endpoint Availability  * Accounting Plus: 🇪🇸 * Accounting Standard: 🇪🇸 * Accounting Start: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = sage.SalesCorrectiveInvoicesApi(api_client)
    key = 'key_example' # str | The Sales Corrective Invoice Key.
sales_corrective_invoices = sage.PutSalesCorrectiveInvoices() # PutSalesCorrectiveInvoices | 

    try:
        # Updates a Sales Corrective Invoice
        api_response = api_instance.put_sales_corrective_invoices_key(key, sales_corrective_invoices)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesCorrectiveInvoicesApi->put_sales_corrective_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Corrective Invoice Key. | 
 **sales_corrective_invoices** | [**PutSalesCorrectiveInvoices**](PutSalesCorrectiveInvoices.md)|  | 

### Return type

[**SalesCorrectiveInvoice**](SalesCorrectiveInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Sales Corrective Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

