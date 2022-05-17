# EmailSettings

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_messages** | [**list[DefaultMessages]**](DefaultMessages.md) | The default email messages for the businesses per message type and locale. | [optional] 
**pdf_attached** | **bool** | Indicates whether PDFs are always attached as part of sending emails for a business | [optional] 
**send_bcc** | **bool** | Indicates whether the user should always be sent a copy when sending a document via email | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


