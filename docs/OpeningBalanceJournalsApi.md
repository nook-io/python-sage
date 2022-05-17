# sage.OpeningBalanceJournalsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_opening_balance_journals_key**](OpeningBalanceJournalsApi.md#delete_opening_balance_journals_key) | **DELETE** /opening_balance_journals/{key} | Deletes a Opening Balance Journal
[**get_opening_balance_journals**](OpeningBalanceJournalsApi.md#get_opening_balance_journals) | **GET** /opening_balance_journals | Returns all Opening Balance Journals
[**get_opening_balance_journals_key**](OpeningBalanceJournalsApi.md#get_opening_balance_journals_key) | **GET** /opening_balance_journals/{key} | Returns a Opening Balance Journal
[**post_opening_balance_journals**](OpeningBalanceJournalsApi.md#post_opening_balance_journals) | **POST** /opening_balance_journals | Creates a Opening Balance Journal


# **delete_opening_balance_journals_key**
> delete_opening_balance_journals_key(key)

Deletes a Opening Balance Journal

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, `Contacts`, `Journals`, `Settings`, `Bank`, `Statutory Reporting`, `Products & Services`, and `Reporting`: Full Access

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
    api_instance = sage.OpeningBalanceJournalsApi(api_client)
    key = 'key_example' # str | The Opening Balance Journal Key.

    try:
        # Deletes a Opening Balance Journal
        api_instance.delete_opening_balance_journals_key(key)
    except ApiException as e:
        print("Exception when calling OpeningBalanceJournalsApi->delete_opening_balance_journals_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Opening Balance Journal Key. | 

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
**204** | Deletes a Opening Balance Journal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opening_balance_journals**
> list[OpeningBalanceJournal] get_opening_balance_journals(items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Opening Balance Journals

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, `Contacts`, `Journals`, `Settings`, `Bank`, `Statutory Reporting`, `Products & Services`, and `Reporting`: Full Access, Read Only

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
    api_instance = sage.OpeningBalanceJournalsApi(api_client)
    items_per_page = 20 # int | Returns the given number of Journal Opening Balances per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Journal Opening Balances (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Journal Opening Balances (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Opening Balance Journals
        api_response = api_instance.get_opening_balance_journals(items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpeningBalanceJournalsApi->get_opening_balance_journals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**| Returns the given number of Journal Opening Balances per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Journal Opening Balances | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Journal Opening Balances (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[OpeningBalanceJournal]**](OpeningBalanceJournal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Opening Balance Journals |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opening_balance_journals_key**
> OpeningBalanceJournal get_opening_balance_journals_key(key, attributes=attributes)

Returns a Opening Balance Journal

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, `Contacts`, `Journals`, `Settings`, `Bank`, `Statutory Reporting`, `Products & Services`, and `Reporting`: Full Access, Read Only

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
    api_instance = sage.OpeningBalanceJournalsApi(api_client)
    key = 'key_example' # str | The Opening Balance Journal Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Journal Opening Balance (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Opening Balance Journal
        api_response = api_instance.get_opening_balance_journals_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpeningBalanceJournalsApi->get_opening_balance_journals_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Opening Balance Journal Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Journal Opening Balance (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**OpeningBalanceJournal**](OpeningBalanceJournal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Opening Balance Journal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_opening_balance_journals**
> OpeningBalanceJournal post_opening_balance_journals(opening_balance_journals)

Creates a Opening Balance Journal

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Sales`, `Purchases`, `Contacts`, `Journals`, `Settings`, `Bank`, `Statutory Reporting`, `Products & Services`, and `Reporting`: Full Access

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
    api_instance = sage.OpeningBalanceJournalsApi(api_client)
    opening_balance_journals = sage.PostOpeningBalanceJournals() # PostOpeningBalanceJournals | 

    try:
        # Creates a Opening Balance Journal
        api_response = api_instance.post_opening_balance_journals(opening_balance_journals)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpeningBalanceJournalsApi->post_opening_balance_journals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opening_balance_journals** | [**PostOpeningBalanceJournals**](PostOpeningBalanceJournals.md)|  | 

### Return type

[**OpeningBalanceJournal**](OpeningBalanceJournal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Opening Balance Journal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

