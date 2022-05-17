# Journal

  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Journals`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**transaction** | [**Base**](Base.md) |  | [optional] 
**transaction_type** | [**Base**](Base.md) |  | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**date** | **date** | The date of the journal | [optional] 
**reference** | **str** | A reference for the journal | [optional] 
**description** | **str** | A description of the journal | [optional] 
**total** | **float** | The total for the journal | [optional] 
**journal_code** | [**JournalCode**](JournalCode.md) |  | [optional] 
**journal_lines** | [**list[JournalLine]**](JournalLine.md) | The journal lines | [optional] 
**migrated** | **bool** | Indicates if the journal was migrated from another system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


