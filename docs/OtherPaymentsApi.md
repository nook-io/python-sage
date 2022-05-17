# sage.OtherPaymentsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_other_payments_key**](OtherPaymentsApi.md#delete_other_payments_key) | **DELETE** /other_payments/{key} | Deletes a Other Payment
[**get_other_payments**](OtherPaymentsApi.md#get_other_payments) | **GET** /other_payments | Returns all Other Payments
[**get_other_payments_key**](OtherPaymentsApi.md#get_other_payments_key) | **GET** /other_payments/{key} | Returns a Other Payment
[**post_other_payments**](OtherPaymentsApi.md#post_other_payments) | **POST** /other_payments | Creates a Other Payment
[**put_other_payments_key**](OtherPaymentsApi.md#put_other_payments_key) | **PUT** /other_payments/{key} | Updates a Other Payment


# **delete_other_payments_key**
> delete_other_payments_key(key)

Deletes a Other Payment

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
    api_instance = sage.OtherPaymentsApi(api_client)
    key = 'key_example' # str | The Other Payment Key.

    try:
        # Deletes a Other Payment
        api_instance.delete_other_payments_key(key)
    except ApiException as e:
        print("Exception when calling OtherPaymentsApi->delete_other_payments_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Other Payment Key. | 

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
**204** | Deletes a Other Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_other_payments**
> list[OtherPayment] get_other_payments(bank_account_id=bank_account_id, contact_id=contact_id, deleted_since=deleted_since, from_date=from_date, has_attachments=has_attachments, to_date=to_date, transaction_type_id=transaction_type_id, updated_or_created_since=updated_or_created_since, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)

Returns all Other Payments

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
    api_instance = sage.OtherPaymentsApi(api_client)
    bank_account_id = 'bank_account_id_example' # str | Use this to filter by bank account id (optional)
contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Payments deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Payments dates (optional)
has_attachments = True # bool | Use this to filter Payments by whether they have attachments or not (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Payments dates (optional)
transaction_type_id = 'transaction_type_id_example' # str | Use this to filter by transaction type id (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Payments changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
items_per_page = 20 # int | Returns the given number of Payments per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Payments (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Payments (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
sort = 'sort_example' # str | Order by a given attribute (required) and direction (optional; `asc` or `desc`; defaults to `asc`). Available attributes are: created_at, updated_at, date  Example: `sort=created_at` or `sort=created_at:desc` (optional)

    try:
        # Returns all Other Payments
        api_response = api_instance.get_other_payments(bank_account_id=bank_account_id, contact_id=contact_id, deleted_since=deleted_since, from_date=from_date, has_attachments=has_attachments, to_date=to_date, transaction_type_id=transaction_type_id, updated_or_created_since=updated_or_created_since, items_per_page=items_per_page, page=page, attributes=attributes, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OtherPaymentsApi->get_other_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**| Use this to filter by bank account id | [optional] 
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Payments deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **from_date** | **datetime**| Use this to filter by Payments dates | [optional] 
 **has_attachments** | **bool**| Use this to filter Payments by whether they have attachments or not | [optional] 
 **to_date** | **datetime**| Use this to filter by Payments dates | [optional] 
 **transaction_type_id** | **str**| Use this to filter by transaction type id | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Payments changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **items_per_page** | **int**| Returns the given number of Payments per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Payments | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Payments (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **sort** | **str**| Order by a given attribute (required) and direction (optional; &#x60;asc&#x60; or &#x60;desc&#x60;; defaults to &#x60;asc&#x60;). Available attributes are: created_at, updated_at, date  Example: &#x60;sort&#x3D;created_at&#x60; or &#x60;sort&#x3D;created_at:desc&#x60; | [optional] 

### Return type

[**list[OtherPayment]**](OtherPayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Other Payments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_other_payments_key**
> OtherPayment get_other_payments_key(key, nested_attributes=nested_attributes, attributes=attributes)

Returns a Other Payment

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
    api_instance = sage.OtherPaymentsApi(api_client)
    key = 'key_example' # str | The Other Payment Key.
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Payment (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Payment (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Other Payment
        api_response = api_instance.get_other_payments_key(key, nested_attributes=nested_attributes, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OtherPaymentsApi->get_other_payments_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Other Payment Key. | 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Payment (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Payment (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**OtherPayment**](OtherPayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Other Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_other_payments**
> OtherPayment post_other_payments(other_payments)

Creates a Other Payment

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
    api_instance = sage.OtherPaymentsApi(api_client)
    other_payments = sage.PostOtherPayments() # PostOtherPayments | 

    try:
        # Creates a Other Payment
        api_response = api_instance.post_other_payments(other_payments)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OtherPaymentsApi->post_other_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_payments** | [**PostOtherPayments**](PostOtherPayments.md)|  | 

### Return type

[**OtherPayment**](OtherPayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Other Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_other_payments_key**
> OtherPayment put_other_payments_key(key, other_payments)

Updates a Other Payment

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
    api_instance = sage.OtherPaymentsApi(api_client)
    key = 'key_example' # str | The Other Payment Key.
other_payments = sage.PutOtherPayments() # PutOtherPayments | 

    try:
        # Updates a Other Payment
        api_response = api_instance.put_other_payments_key(key, other_payments)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OtherPaymentsApi->put_other_payments_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Other Payment Key. | 
 **other_payments** | [**PutOtherPayments**](PutOtherPayments.md)|  | 

### Return type

[**OtherPayment**](OtherPayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Other Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

