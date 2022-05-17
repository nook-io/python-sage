# JournalLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**ledger_account** | [**LedgerAccount**](LedgerAccount.md) |  | [optional] 
**details** | **str** | A description of the journal line | [optional] 
**debit** | **float** | The debit amount of the journal line | [optional] 
**credit** | **float** | The credit amount of the journal line | [optional] 
**include_on_tax_return** | **bool** | Indicates whether the journal line should affect the tax return | [optional] 
**tax_reconciled** | **bool** | Indicates if the journal line is tax reconciled or not. | [optional] 
**cleared** | **bool** | Indicates if the journal line is cleared or not.  Will be true when a journal item has been matched with a bank feed or statement.  | [optional] 
**bank_reconciled** | **bool** | Indicates if the journal line is bank reconciled or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


