# sage.ContactsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_contacts_key**](ContactsApi.md#delete_contacts_key) | **DELETE** /contacts/{key} | Deletes a Contact
[**get_contacts**](ContactsApi.md#get_contacts) | **GET** /contacts | Returns all Contacts
[**get_contacts_key**](ContactsApi.md#get_contacts_key) | **GET** /contacts/{key} | Returns a Contact
[**post_contacts**](ContactsApi.md#post_contacts) | **POST** /contacts | Creates a Contact
[**put_contacts_key**](ContactsApi.md#put_contacts_key) | **PUT** /contacts/{key} | Updates a Contact


# **delete_contacts_key**
> delete_contacts_key(key)

Deletes a Contact

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
    api_instance = sage.ContactsApi(api_client)
    key = 'key_example' # str | The Contact Key.

    try:
        # Deletes a Contact
        api_instance.delete_contacts_key(key)
    except ApiException as e:
        print("Exception when calling ContactsApi->delete_contacts_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Key. | 

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
**204** | Deletes a Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> list[Contact] get_contacts(updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, contact_type_id=contact_type_id, exclude_system=exclude_system, nested_attributes=nested_attributes, show_balance=show_balance, context_date=context_date, search=search, email=email, show_unfinished_recurring_invoices_status=show_unfinished_recurring_invoices_status, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Contacts

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
    api_instance = sage.ContactsApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Contacts changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Contacts deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
contact_type_id = 'contact_type_id_example' # str | Use this to filter by contact type id (optional)
exclude_system = True # bool | Use this to filter out system entities, not applicable for transaction creation (optional)
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Contacts (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
show_balance = True # bool | Use this to display the balance for a contact. (optional)
context_date = '2013-10-20' # date | Use this to determine the correct tax treatment for a contact on a given date. (optional)
search = 'search_example' # str | Use this to filter by the contact name, company name or reference. (optional)
email = 'email_example' # str | Use this to filter by the contact person email address. (optional)
show_unfinished_recurring_invoices_status = True # bool |  (optional)
items_per_page = 20 # int | Returns the given number of Contacts per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Contacts (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Contacts (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Contacts
        api_response = api_instance.get_contacts(updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, contact_type_id=contact_type_id, exclude_system=exclude_system, nested_attributes=nested_attributes, show_balance=show_balance, context_date=context_date, search=search, email=email, show_unfinished_recurring_invoices_status=show_unfinished_recurring_invoices_status, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Contacts changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Contacts deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **contact_type_id** | **str**| Use this to filter by contact type id | [optional] 
 **exclude_system** | **bool**| Use this to filter out system entities, not applicable for transaction creation | [optional] 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Contacts (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **show_balance** | **bool**| Use this to display the balance for a contact. | [optional] 
 **context_date** | **date**| Use this to determine the correct tax treatment for a contact on a given date. | [optional] 
 **search** | **str**| Use this to filter by the contact name, company name or reference. | [optional] 
 **email** | **str**| Use this to filter by the contact person email address. | [optional] 
 **show_unfinished_recurring_invoices_status** | **bool**|  | [optional] 
 **items_per_page** | **int**| Returns the given number of Contacts per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Contacts | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Contacts (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[Contact]**](Contact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Contacts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_key**
> Contact get_contacts_key(key, nested_attributes=nested_attributes, show_balance=show_balance, context_date=context_date, show_unfinished_recurring_invoices_status=show_unfinished_recurring_invoices_status, attributes=attributes)

Returns a Contact

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
    api_instance = sage.ContactsApi(api_client)
    key = 'key_example' # str | The Contact Key.
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Contact (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
show_balance = True # bool | Use this to display the balance for a contact. (optional)
context_date = '2013-10-20' # date | Use this to determine the correct tax treatment for a contact on a given date. (optional)
show_unfinished_recurring_invoices_status = True # bool |  (optional) (default to True)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Contact (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Contact
        api_response = api_instance.get_contacts_key(key, nested_attributes=nested_attributes, show_balance=show_balance, context_date=context_date, show_unfinished_recurring_invoices_status=show_unfinished_recurring_invoices_status, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->get_contacts_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Key. | 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Contact (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **show_balance** | **bool**| Use this to display the balance for a contact. | [optional] 
 **context_date** | **date**| Use this to determine the correct tax treatment for a contact on a given date. | [optional] 
 **show_unfinished_recurring_invoices_status** | **bool**|  | [optional] [default to True]
 **attributes** | **str**| Specify the attributes that you want to expose for the Contact (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**Contact**](Contact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_contacts**
> Contact post_contacts(contacts)

Creates a Contact

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
    api_instance = sage.ContactsApi(api_client)
    contacts = sage.PostContacts() # PostContacts | 

    try:
        # Creates a Contact
        api_response = api_instance.post_contacts(contacts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->post_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contacts** | [**PostContacts**](PostContacts.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_contacts_key**
> Contact put_contacts_key(key, contacts)

Updates a Contact

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
    api_instance = sage.ContactsApi(api_client)
    key = 'key_example' # str | The Contact Key.
contacts = sage.PutContacts() # PutContacts | 

    try:
        # Updates a Contact
        api_response = api_instance.put_contacts_key(key, contacts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->put_contacts_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Key. | 
 **contacts** | [**PutContacts**](PutContacts.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

