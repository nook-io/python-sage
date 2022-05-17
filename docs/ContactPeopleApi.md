# sage.ContactPeopleApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_contact_persons_key**](ContactPeopleApi.md#delete_contact_persons_key) | **DELETE** /contact_persons/{key} | Deletes a Contact Person
[**get_contact_persons**](ContactPeopleApi.md#get_contact_persons) | **GET** /contact_persons | Returns all Contact People
[**get_contact_persons_key**](ContactPeopleApi.md#get_contact_persons_key) | **GET** /contact_persons/{key} | Returns a Contact Person
[**post_contact_persons**](ContactPeopleApi.md#post_contact_persons) | **POST** /contact_persons | Creates a Contact Person
[**put_contact_persons_key**](ContactPeopleApi.md#put_contact_persons_key) | **PUT** /contact_persons/{key} | Updates a Contact Person


# **delete_contact_persons_key**
> delete_contact_persons_key(key)

Deletes a Contact Person

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Full Access

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
    api_instance = sage.ContactPeopleApi(api_client)
    key = 'key_example' # str | The Contact Person Key.

    try:
        # Deletes a Contact Person
        api_instance.delete_contact_persons_key(key)
    except ApiException as e:
        print("Exception when calling ContactPeopleApi->delete_contact_persons_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Person Key. | 

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
**204** | Deletes a Contact Person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_persons**
> list[ContactPerson] get_contact_persons(address_id=address_id, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, contact_id=contact_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Contact People

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.ContactPeopleApi(api_client)
    address_id = 'address_id_example' # str | Use this to filter by address id (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Address Contacts changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Address Contacts deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
items_per_page = 20 # int | Returns the given number of Address Contacts per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Address Contacts (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Address Contacts (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Contact People
        api_response = api_instance.get_contact_persons(address_id=address_id, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, contact_id=contact_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPeopleApi->get_contact_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **str**| Use this to filter by address id | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Address Contacts changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Address Contacts deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **items_per_page** | **int**| Returns the given number of Address Contacts per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Address Contacts | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Address Contacts (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[ContactPerson]**](ContactPerson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Contact People |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_persons_key**
> ContactPerson get_contact_persons_key(key, nested_attributes=nested_attributes, attributes=attributes)

Returns a Contact Person

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access * Area: `Bank`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.ContactPeopleApi(api_client)
    key = 'key_example' # str | The Contact Person Key.
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Address Contact (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Address Contact (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Contact Person
        api_response = api_instance.get_contact_persons_key(key, nested_attributes=nested_attributes, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPeopleApi->get_contact_persons_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Person Key. | 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Address Contact (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Address Contact (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**ContactPerson**](ContactPerson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Contact Person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_contact_persons**
> ContactPerson post_contact_persons(contact_persons)

Creates a Contact Person

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Restricted Access, Full Access

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
    api_instance = sage.ContactPeopleApi(api_client)
    contact_persons = sage.PostContactPersons() # PostContactPersons | 

    try:
        # Creates a Contact Person
        api_response = api_instance.post_contact_persons(contact_persons)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPeopleApi->post_contact_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_persons** | [**PostContactPersons**](PostContactPersons.md)|  | 

### Return type

[**ContactPerson**](ContactPerson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Contact Person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_contact_persons_key**
> ContactPerson put_contact_persons_key(key, contact_persons)

Updates a Contact Person

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Restricted Access, Full Access

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
    api_instance = sage.ContactPeopleApi(api_client)
    key = 'key_example' # str | The Contact Person Key.
contact_persons = sage.PutContactPersons() # PutContactPersons | 

    try:
        # Updates a Contact Person
        api_response = api_instance.put_contact_persons_key(key, contact_persons)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPeopleApi->put_contact_persons_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Person Key. | 
 **contact_persons** | [**PutContactPersons**](PutContactPersons.md)|  | 

### Return type

[**ContactPerson**](ContactPerson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Contact Person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

