# sage.AttachmentsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachments_key**](AttachmentsApi.md#delete_attachments_key) | **DELETE** /attachments/{key} | Deletes a Attachment
[**get_attachments**](AttachmentsApi.md#get_attachments) | **GET** /attachments | Returns all Attachments
[**get_attachments_key**](AttachmentsApi.md#get_attachments_key) | **GET** /attachments/{key} | Returns a Attachment
[**get_attachments_key_file**](AttachmentsApi.md#get_attachments_key_file) | **GET** /attachments/{key}/file | Returns an Attachment File
[**post_attachments**](AttachmentsApi.md#post_attachments) | **POST** /attachments | Creates a Attachment
[**put_attachments_key**](AttachmentsApi.md#put_attachments_key) | **PUT** /attachments/{key} | Updates a Attachment


# **delete_attachments_key**
> delete_attachments_key(key)

Deletes a Attachment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Restricted Access, Full Access * Area: `Purchases`: Restricted Access, Full Access

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
    api_instance = sage.AttachmentsApi(api_client)
    key = 'key_example' # str | The Attachment Key.

    try:
        # Deletes a Attachment
        api_instance.delete_attachments_key(key)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->delete_attachments_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Attachment Key. | 

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
**204** | Deletes a Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments**
> list[Attachment] get_attachments(attachment_context_id=attachment_context_id, attachment_context_type_id=attachment_context_type_id, legacy_attachment_context_type=legacy_attachment_context_type, legacy_attachment_context_id=legacy_attachment_context_id, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Attachments

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.AttachmentsApi(api_client)
    attachment_context_id = 'attachment_context_id_example' # str | Use this to filter Attachments by attachment_context_id. Requires filtering by attachment_context_type_id as well (optional)
attachment_context_type_id = 'attachment_context_type_id_example' # str | Use this to filter Attachments by attachment_context_type_id. Requires filtering by attachment_context_id as well (optional)
legacy_attachment_context_type = 'legacy_attachment_context_type_example' # str |  (optional)
legacy_attachment_context_id = 56 # int |  (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Attachments changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Attachments deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
items_per_page = 20 # int | Returns the given number of Attachments per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Attachments (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Attachments (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Attachments
        api_response = api_instance.get_attachments(attachment_context_id=attachment_context_id, attachment_context_type_id=attachment_context_type_id, legacy_attachment_context_type=legacy_attachment_context_type, legacy_attachment_context_id=legacy_attachment_context_id, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_context_id** | **str**| Use this to filter Attachments by attachment_context_id. Requires filtering by attachment_context_type_id as well | [optional] 
 **attachment_context_type_id** | **str**| Use this to filter Attachments by attachment_context_type_id. Requires filtering by attachment_context_id as well | [optional] 
 **legacy_attachment_context_type** | **str**|  | [optional] 
 **legacy_attachment_context_id** | **int**|  | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Attachments changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Attachments deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **items_per_page** | **int**| Returns the given number of Attachments per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Attachments | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Attachments (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[Attachment]**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments_key**
> Attachment get_attachments_key(key, attributes=attributes)

Returns a Attachment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.AttachmentsApi(api_client)
    key = 'key_example' # str | The Attachment Key.
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Attachment (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Attachment
        api_response = api_instance.get_attachments_key(key, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachments_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Attachment Key. | 
 **attributes** | **str**| Specify the attributes that you want to expose for the Attachment (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments_key_file**
> Attachment get_attachments_key_file(accept, key)

Returns an Attachment File

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = sage.AttachmentsApi(api_client)
    accept = 'accept_example' # str | Specify the Accept header of the request. It must always be set to `application/octet-stream` for retrieving files. 
key = 'key_example' # str | The Attachment Key.

    try:
        # Returns an Attachment File
        api_response = api_instance.get_attachments_key_file(accept, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachments_key_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specify the Accept header of the request. It must always be set to &#x60;application/octet-stream&#x60; for retrieving files.  | 
 **key** | **str**| The Attachment Key. | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an Attachment File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attachments**
> Attachment post_attachments(attachments)

Creates a Attachment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Restricted Access, Full Access * Area: `Purchases`: Restricted Access, Full Access

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
    api_instance = sage.AttachmentsApi(api_client)
    attachments = sage.PostAttachments() # PostAttachments | 

    try:
        # Creates a Attachment
        api_response = api_instance.post_attachments(attachments)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->post_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachments** | [**PostAttachments**](PostAttachments.md)|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_attachments_key**
> Attachment put_attachments_key(key, attachments)

Updates a Attachment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Restricted Access, Full Access * Area: `Purchases`: Restricted Access, Full Access

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
    api_instance = sage.AttachmentsApi(api_client)
    key = 'key_example' # str | The Attachment Key.
attachments = sage.PutAttachments() # PutAttachments | 

    try:
        # Updates a Attachment
        api_response = api_instance.put_attachments_key(key, attachments)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi->put_attachments_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Attachment Key. | 
 **attachments** | [**PutAttachments**](PutAttachments.md)|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

