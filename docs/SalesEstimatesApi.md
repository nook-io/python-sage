# sage.SalesEstimatesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_estimates_key**](SalesEstimatesApi.md#delete_sales_estimates_key) | **DELETE** /sales_estimates/{key} | Deletes a Sales Estimate
[**get_sales_estimates**](SalesEstimatesApi.md#get_sales_estimates) | **GET** /sales_estimates | Returns all Sales Estimates
[**get_sales_estimates_key**](SalesEstimatesApi.md#get_sales_estimates_key) | **GET** /sales_estimates/{key} | Returns a Sales Estimate
[**post_sales_estimates**](SalesEstimatesApi.md#post_sales_estimates) | **POST** /sales_estimates | Creates a Sales Estimate
[**put_sales_estimates_key**](SalesEstimatesApi.md#put_sales_estimates_key) | **PUT** /sales_estimates/{key} | Updates a Sales Estimate


# **delete_sales_estimates_key**
> delete_sales_estimates_key(key)

Deletes a Sales Estimate

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇫🇷, 🇮🇪, 🇬🇧, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access

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
    api_instance = sage.SalesEstimatesApi(api_client)
    key = 'key_example' # str | The Sales Estimate Key.

    try:
        # Deletes a Sales Estimate
        api_instance.delete_sales_estimates_key(key)
    except ApiException as e:
        print("Exception when calling SalesEstimatesApi->delete_sales_estimates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Estimate Key. | 

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
**204** | Deletes a Sales Estimate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_estimates**
> list[SalesEstimate] get_sales_estimates(contact_id=contact_id, search=search, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Sales Estimates

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
    api_instance = sage.SalesEstimatesApi(api_client)
    contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
search = 'search_example' # str | Use this to filter by the estimate reference or contact name. (optional)
status_id = 'status_id_example' # str | Use this to filter by status id (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Estimates dates (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Use this to filter by Sales Estimates dates (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Sales Estimates changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
has_attachments = True # bool | Use this to filter Sales Estimates by whether they have attachments or not (optional)
items_per_page = 20 # int | Returns the given number of Sales Estimates per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Sales Estimates (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Estimates (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Sales Estimates
        api_response = api_instance.get_sales_estimates(contact_id=contact_id, search=search, status_id=status_id, from_date=from_date, to_date=to_date, updated_or_created_since=updated_or_created_since, has_attachments=has_attachments, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesEstimatesApi->get_sales_estimates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **search** | **str**| Use this to filter by the estimate reference or contact name. | [optional] 
 **status_id** | **str**| Use this to filter by status id | [optional] 
 **from_date** | **datetime**| Use this to filter by Sales Estimates dates | [optional] 
 **to_date** | **datetime**| Use this to filter by Sales Estimates dates | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Sales Estimates changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **has_attachments** | **bool**| Use this to filter Sales Estimates by whether they have attachments or not | [optional] 
 **items_per_page** | **int**| Returns the given number of Sales Estimates per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Sales Estimates | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Estimates (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[SalesEstimate]**](SalesEstimate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Sales Estimates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_estimates_key**
> SalesEstimate get_sales_estimates_key(key, nested_attributes=nested_attributes, attributes=attributes)

Returns a Sales Estimate

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
    api_instance = sage.SalesEstimatesApi(api_client)
    key = 'key_example' # str | The Sales Estimate Key.
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Sales Estimate (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Sales Estimate (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Sales Estimate
        api_response = api_instance.get_sales_estimates_key(key, nested_attributes=nested_attributes, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesEstimatesApi->get_sales_estimates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Estimate Key. | 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Sales Estimate (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Sales Estimate (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**SalesEstimate**](SalesEstimate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Sales Estimate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_estimates**
> SalesEstimate post_sales_estimates(sales_estimates)

Creates a Sales Estimate

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
    api_instance = sage.SalesEstimatesApi(api_client)
    sales_estimates = sage.PostSalesEstimates() # PostSalesEstimates | 

    try:
        # Creates a Sales Estimate
        api_response = api_instance.post_sales_estimates(sales_estimates)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesEstimatesApi->post_sales_estimates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_estimates** | [**PostSalesEstimates**](PostSalesEstimates.md)|  | 

### Return type

[**SalesEstimate**](SalesEstimate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Sales Estimate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_estimates_key**
> SalesEstimate put_sales_estimates_key(key, sales_estimates)

Updates a Sales Estimate

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
    api_instance = sage.SalesEstimatesApi(api_client)
    key = 'key_example' # str | The Sales Estimate Key.
sales_estimates = sage.PutSalesEstimates() # PutSalesEstimates | 

    try:
        # Updates a Sales Estimate
        api_response = api_instance.put_sales_estimates_key(key, sales_estimates)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SalesEstimatesApi->put_sales_estimates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Sales Estimate Key. | 
 **sales_estimates** | [**PutSalesEstimates**](PutSalesEstimates.md)|  | 

### Return type

[**SalesEstimate**](SalesEstimate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Sales Estimate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

