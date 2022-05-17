# BankReconciliation

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**bank_account** | [**Base**](Base.md) |  | [optional] 
**statement_date** | **date** | The date of the bank reconciliation | [optional] 
**statement_end_balance** | **float** | The statement end balance for the reconciliation | [optional] 
**reference** | **str** | A reference for the bank reconciliation | [optional] 
**total_received** | **float** | The total amount received | [optional] 
**total_paid** | **float** | The total amount paid | [optional] 
**starting_balance** | **float** | The starting balance of the bank reconciliation | [optional] 
**closing_balance** | **float** | The closing balance of the bank reconciliation | [optional] 
**reconciled_balance** | **float** | The reconciled balance of the bank reconciliation | [optional] 
**balance_difference** | **float** | The difference between the statement end balance and the reconciled balance | [optional] 
**status** | [**BankReconciliationStatus**](BankReconciliationStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


