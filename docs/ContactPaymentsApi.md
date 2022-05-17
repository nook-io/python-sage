# sage.ContactPaymentsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_contact_payments_key**](ContactPaymentsApi.md#delete_contact_payments_key) | **DELETE** /contact_payments/{key} | Deletes a Contact Payment
[**get_contact_payments**](ContactPaymentsApi.md#get_contact_payments) | **GET** /contact_payments | Returns all Contact Payments
[**get_contact_payments_key**](ContactPaymentsApi.md#get_contact_payments_key) | **GET** /contact_payments/{key} | Returns a Contact Payment
[**post_contact_payments**](ContactPaymentsApi.md#post_contact_payments) | **POST** /contact_payments | Creates a Contact Payment
[**put_contact_payments_key**](ContactPaymentsApi.md#put_contact_payments_key) | **PUT** /contact_payments/{key} | Updates a Contact Payment


# **delete_contact_payments_key**
> delete_contact_payments_key(key)

Deletes a Contact Payment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access

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
    api_instance = sage.ContactPaymentsApi(api_client)
    key = 'key_example' # str | The Contact Payment Key.

    try:
        # Deletes a Contact Payment
        api_instance.delete_contact_payments_key(key)
    except ApiException as e:
        print("Exception when calling ContactPaymentsApi->delete_contact_payments_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Payment Key. | 

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
**204** | Deletes a Contact Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_payments**
> list[ContactPayment] get_contact_payments(contact_id=contact_id, bank_account_id=bank_account_id, transaction_type_id=transaction_type_id, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, from_date=from_date, to_date=to_date, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Contact Payments

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.ContactPaymentsApi(api_client)
    contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
bank_account_id = 'bank_account_id_example' # str | Use this to filter by bank account id (optional)
transaction_type_id = 'transaction_type_id_example' # str | Use this to filter by transaction type id (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Artefact Payments changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Artefact Payments deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Artefact Payments dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Artefact Payments dates (optional)
items_per_page = 20 # int | Returns the given number of Artefact Payments per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Artefact Payments (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Artefact Payments (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Contact Payments
        api_response = api_instance.get_contact_payments(contact_id=contact_id, bank_account_id=bank_account_id, transaction_type_id=transaction_type_id, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, from_date=from_date, to_date=to_date, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPaymentsApi->get_contact_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **bank_account_id** | **str**| Use this to filter by bank account id | [optional] 
 **transaction_type_id** | **str**| Use this to filter by transaction type id | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Artefact Payments changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Artefact Payments deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **from_date** | **datetime**| Use this to filter by Artefact Payments dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Artefact Payments dates | [optional] 
 **items_per_page** | **int**| Returns the given number of Artefact Payments per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Artefact Payments | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Artefact Payments (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[ContactPayment]**](ContactPayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Contact Payments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_payments_key**
> ContactPayment get_contact_payments_key(key, attributes=attributes)

Returns a Contact Payment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.ContactPaymentsApi(api_client)
    key = 'key_example' # str | The Contact Payment Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Artefact Payment (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Contact Payment
        api_response = api_instance.get_contact_payments_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPaymentsApi->get_contact_payments_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Payment Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Artefact Payment (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**ContactPayment**](ContactPayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Contact Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_contact_payments**
> ContactPayment post_contact_payments(contact_payments)

Creates a Contact Payment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Restricted Access, Full Access

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
    api_instance = sage.ContactPaymentsApi(api_client)
    contact_payments = sage.PostContactPayments() # PostContactPayments | 

    try:
        # Creates a Contact Payment
        api_response = api_instance.post_contact_payments(contact_payments)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPaymentsApi->post_contact_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_payments** | [**PostContactPayments**](PostContactPayments.md)|  | 

### Return type

[**ContactPayment**](ContactPayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Contact Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_contact_payments_key**
> ContactPayment put_contact_payments_key(key, contact_payments)

Updates a Contact Payment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Restricted Access, Full Access

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
    api_instance = sage.ContactPaymentsApi(api_client)
    key = 'key_example' # str | The Contact Payment Key.
contact_payments = sage.PutContactPayments() # PutContactPayments | 

    try:
        # Updates a Contact Payment
        api_response = api_instance.put_contact_payments_key(key, contact_payments)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPaymentsApi->put_contact_payments_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Payment Key. | 
 **contact_payments** | [**PutContactPayments**](PutContactPayments.md)|  | 

### Return type

[**ContactPayment**](ContactPayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Contact Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

