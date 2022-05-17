# sage.BankReconciliationsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bank_reconciliations**](BankReconciliationsApi.md#get_bank_reconciliations) | **GET** /bank_reconciliations | Returns all Bank Reconciliations
[**get_bank_reconciliations_key**](BankReconciliationsApi.md#get_bank_reconciliations_key) | **GET** /bank_reconciliations/{key} | Returns a Bank Reconciliation
[**post_bank_reconciliations**](BankReconciliationsApi.md#post_bank_reconciliations) | **POST** /bank_reconciliations | Creates a Bank Reconciliation
[**put_bank_reconciliations_key**](BankReconciliationsApi.md#put_bank_reconciliations_key) | **PUT** /bank_reconciliations/{key} | Updates a Bank Reconciliation


# **get_bank_reconciliations**
> list[BankReconciliation] get_bank_reconciliations(updated_or_created_since=updated_or_created_since, bank_account_id=bank_account_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Bank Reconciliations

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.BankReconciliationsApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Bank Reconciliations changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
bank_account_id = 'bank_account_id_example' # str | Use this to filter by bank account id (optional)
items_per_page = 20 # int | Returns the given number of Bank Reconciliations per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Bank Reconciliations (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Bank Reconciliations (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Bank Reconciliations
        api_response = api_instance.get_bank_reconciliations(updated_or_created_since=updated_or_created_since, bank_account_id=bank_account_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankReconciliationsApi->get_bank_reconciliations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Bank Reconciliations changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **bank_account_id** | **str**| Use this to filter by bank account id | [optional] 
 **items_per_page** | **int**| Returns the given number of Bank Reconciliations per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Bank Reconciliations | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Bank Reconciliations (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[BankReconciliation]**](BankReconciliation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Bank Reconciliations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_reconciliations_key**
> BankReconciliation get_bank_reconciliations_key(key, attributes=attributes)

Returns a Bank Reconciliation

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access, Read Only, Restricted Access

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
    api_instance = sage.BankReconciliationsApi(api_client)
    key = 'key_example' # str | The Bank Reconciliation Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Bank Reconciliation (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Bank Reconciliation
        api_response = api_instance.get_bank_reconciliations_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankReconciliationsApi->get_bank_reconciliations_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Bank Reconciliation Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Bank Reconciliation (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**BankReconciliation**](BankReconciliation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Bank Reconciliation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bank_reconciliations**
> BankReconciliation post_bank_reconciliations(bank_reconciliations)

Creates a Bank Reconciliation

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
    api_instance = sage.BankReconciliationsApi(api_client)
    bank_reconciliations = sage.PostBankReconciliations() # PostBankReconciliations | 

    try:
        # Creates a Bank Reconciliation
        api_response = api_instance.post_bank_reconciliations(bank_reconciliations)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankReconciliationsApi->post_bank_reconciliations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_reconciliations** | [**PostBankReconciliations**](PostBankReconciliations.md)|  | 

### Return type

[**BankReconciliation**](BankReconciliation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Bank Reconciliation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bank_reconciliations_key**
> BankReconciliation put_bank_reconciliations_key(key, bank_reconciliations)

Updates a Bank Reconciliation

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
    api_instance = sage.BankReconciliationsApi(api_client)
    key = 'key_example' # str | The Bank Reconciliation Key.
bank_reconciliations = sage.PutBankReconciliations() # PutBankReconciliations | 

    try:
        # Updates a Bank Reconciliation
        api_response = api_instance.put_bank_reconciliations_key(key, bank_reconciliations)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankReconciliationsApi->put_bank_reconciliations_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Bank Reconciliation Key. | 
 **bank_reconciliations** | [**PutBankReconciliations**](PutBankReconciliations.md)|  | 

### Return type

[**BankReconciliation**](BankReconciliation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Bank Reconciliation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

