# BankDeposit

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access
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
**from_bank_account** | [**BankAccount**](BankAccount.md) |  | [optional] 
**to_bank_account** | [**BankAccount**](BankAccount.md) |  | [optional] 
**date** | **date** | User generated date of transaction, not necessarily when it was created | [optional] 
**reference** | **str** | Reference | [optional] 
**cash_amount** | **float** | Cash total in the deposit | [optional] 
**cheque_amount** | **float** | Cheque total in the deposit | [optional] 
**total_amount** | **float** | Total of cash and cheques in the deposit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


