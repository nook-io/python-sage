# Transaction

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Journals`: Read Only, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**date** | **date** | The date of the transaction | [optional] 
**deleted** | **bool** | Indicates whether the transaction has been deleted | [optional] 
**reference** | **str** | The transaction reference | [optional] 
**total** | **float** | The transaction total in the base currency | [optional] 
**total_in_transaction_currency** | **float** | The transaction total in the transaction&#39;s origin&#39;s currency. This is null for some origin types. | [optional] 
**contact** | [**Base**](Base.md) |  | [optional] 
**transaction_type** | [**Base**](Base.md) |  | [optional] 
**origin** | [**TransactionOrigin**](TransactionOrigin.md) |  | [optional] 
**audit_trail_id** | **str** | The original entity that generated the transaction | [optional] 
**number_of_attachments** | **str** | The number of attachments related to the transaction | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


