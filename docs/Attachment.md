# Attachment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**file** | **str** | The base64 encoded representation of the file | [optional] 
**mime_type** | **str** | The mime type of the attachment | [optional] 
**description** | **str** | The description of the attachment | [optional] 
**file_extension** | **str** | The file extension of the attachment | [optional] 
**transaction** | [**Base**](Base.md) |  | [optional] 
**file_size** | **int** | The file size of the attachment in Bytes | [optional] 
**file_name** | **str** | The file name of the attachment | [optional] 
**file_path** | **str** | The file path of the attachment | [optional] 
**attachment_context_type** | [**Base**](Base.md) |  | [optional] 
**attachment_context** | [**Base**](Base.md) |  | [optional] 
**is_public** | **bool** | Flag to determine whether the attachment should be visible to customers | [optional] 
**created_at** | **datetime** | The datetime when the attachment was created | [optional] 
**updated_at** | **datetime** | The datetime when the attachment was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


