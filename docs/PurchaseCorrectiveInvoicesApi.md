# sage.PurchaseCorrectiveInvoicesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_purchase_corrective_invoices_key**](PurchaseCorrectiveInvoicesApi.md#delete_purchase_corrective_invoices_key) | **DELETE** /purchase_corrective_invoices/{key} | Deletes a Purchase Corrective Invoice
[**get_purchase_corrective_invoices**](PurchaseCorrectiveInvoicesApi.md#get_purchase_corrective_invoices) | **GET** /purchase_corrective_invoices | Returns all Purchase Corrective Invoices
[**get_purchase_corrective_invoices_key**](PurchaseCorrectiveInvoicesApi.md#get_purchase_corrective_invoices_key) | **GET** /purchase_corrective_invoices/{key} | Returns a Purchase Corrective Invoice
[**post_purchase_corrective_invoices**](PurchaseCorrectiveInvoicesApi.md#post_purchase_corrective_invoices) | **POST** /purchase_corrective_invoices | Creates a Purchase Corrective Invoice
[**put_purchase_corrective_invoices_key**](PurchaseCorrectiveInvoicesApi.md#put_purchase_corrective_invoices_key) | **PUT** /purchase_corrective_invoices/{key} | Updates a Purchase Corrective Invoice


# **delete_purchase_corrective_invoices_key**
> delete_purchase_corrective_invoices_key(key)

Deletes a Purchase Corrective Invoice

### Endpoint Availability  * Accounting Plus: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access

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
    api_instance = sage.PurchaseCorrectiveInvoicesApi(api_client)
    key = 'key_example' # str | The Purchase Corrective Invoice Key.

    try:
        # Deletes a Purchase Corrective Invoice
        api_instance.delete_purchase_corrective_invoices_key(key)
    except ApiException as e:
        print("Exception when calling PurchaseCorrectiveInvoicesApi->delete_purchase_corrective_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Corrective Invoice Key. | 

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
**204** | Deletes a Purchase Corrective Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_corrective_invoices**
> list[PurchaseCorrectiveInvoice] get_purchase_corrective_invoices(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Purchase Corrective Invoices

### Endpoint Availability  * Accounting Plus: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.PurchaseCorrectiveInvoicesApi(api_client)
    show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
search = 'search_example' # str | Use this to filter by the invoice reference or contact name. (optional)
contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
status_id = 'status_id_example' # str | Use this to filter by status id (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Purchase Corrective Invoices dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Purchase Corrective Invoices dates (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Purchase Corrective Invoices changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Purchase Corrective Invoices deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
has_attachments = True # bool | Use this to filter Purchase Corrective Invoices by whether they have attachments or not (optional)
items_per_page = 20 # int | Returns the given number of Purchase Corrective Invoices per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Purchase Corrective Invoices (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Purchase Corrective Invoices (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date, due_date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Purchase Corrective Invoices
        api_response = api_instance.get_purchase_corrective_invoices(show_payments_allocations=show_payments_allocations, search=search, contact_id=contact_id, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseCorrectiveInvoicesApi->get_purchase_corrective_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **search** | **str**| Use this to filter by the invoice reference or contact name. | [optional] 
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **status_id** | **str**| Use this to filter by status id | [optional] 
 **from_date** | **datetime**| Use this to filter by Purchase Corrective Invoices dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Purchase Corrective Invoices dates | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Purchase Corrective Invoices changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Purchase Corrective Invoices deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **has_attachments** | **bool**| Use this to filter Purchase Corrective Invoices by whether they have attachments or not | [optional] 
 **items_per_page** | **int**| Returns the given number of Purchase Corrective Invoices per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Purchase Corrective Invoices | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Purchase Corrective Invoices (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date, due_date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[PurchaseCorrectiveInvoice]**](PurchaseCorrectiveInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Purchase Corrective Invoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_corrective_invoices_key**
> PurchaseCorrectiveInvoice get_purchase_corrective_invoices_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, attributes=attributes)

Returns a Purchase Corrective Invoice

### Endpoint Availability  * Accounting Plus: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.PurchaseCorrectiveInvoicesApi(api_client)
    key = 'key_example' # str | The Purchase Corrective Invoice Key.
show_payments_allocations = True # bool | Use this to show the artefact's payments and allocations (optional)
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Purchase Corrective Invoice (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Purchase Corrective Invoice (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Purchase Corrective Invoice
        api_response = api_instance.get_purchase_corrective_invoices_key(key, show_payments_allocations=show_payments_allocations, nested_attributes=nested_attributes, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseCorrectiveInvoicesApi->get_purchase_corrective_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Corrective Invoice Key. | 
 **show_payments_allocations** | **bool**| Use this to show the artefact&#39;s payments and allocations | [optional] 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Purchase Corrective Invoice (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Purchase Corrective Invoice (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**PurchaseCorrectiveInvoice**](PurchaseCorrectiveInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Purchase Corrective Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_purchase_corrective_invoices**
> PurchaseCorrectiveInvoice post_purchase_corrective_invoices(purchase_corrective_invoices)

Creates a Purchase Corrective Invoice

### Endpoint Availability  * Accounting Plus: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Restricted Access

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
    api_instance = sage.PurchaseCorrectiveInvoicesApi(api_client)
    purchase_corrective_invoices = sage.PostPurchaseCorrectiveInvoices() # PostPurchaseCorrectiveInvoices | 

    try:
        # Creates a Purchase Corrective Invoice
        api_response = api_instance.post_purchase_corrective_invoices(purchase_corrective_invoices)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseCorrectiveInvoicesApi->post_purchase_corrective_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_corrective_invoices** | [**PostPurchaseCorrectiveInvoices**](PostPurchaseCorrectiveInvoices.md)|  | 

### Return type

[**PurchaseCorrectiveInvoice**](PurchaseCorrectiveInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Purchase Corrective Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_purchase_corrective_invoices_key**
> PurchaseCorrectiveInvoice put_purchase_corrective_invoices_key(key, purchase_corrective_invoices)

Updates a Purchase Corrective Invoice

### Endpoint Availability  * Accounting Plus: 🇪🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Restricted Access

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
    api_instance = sage.PurchaseCorrectiveInvoicesApi(api_client)
    key = 'key_example' # str | The Purchase Corrective Invoice Key.
purchase_corrective_invoices = sage.PutPurchaseCorrectiveInvoices() # PutPurchaseCorrectiveInvoices | 

    try:
        # Updates a Purchase Corrective Invoice
        api_response = api_instance.put_purchase_corrective_invoices_key(key, purchase_corrective_invoices)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PurchaseCorrectiveInvoicesApi->put_purchase_corrective_invoices_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Purchase Corrective Invoice Key. | 
 **purchase_corrective_invoices** | [**PutPurchaseCorrectiveInvoices**](PutPurchaseCorrectiveInvoices.md)|  | 

### Return type

[**PurchaseCorrectiveInvoice**](PurchaseCorrectiveInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Purchase Corrective Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

