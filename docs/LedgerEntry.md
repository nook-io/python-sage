# LedgerEntry

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Journals`: Read Only, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**date** | **date** | The date of the ledger entry | [optional] 
**credit** | **float** | The credit amount of the ledger entry | [optional] 
**debit** | **float** | The debit amount of the ledger entry | [optional] 
**ledger_account** | [**LedgerAccount**](LedgerAccount.md) |  | [optional] 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**deleted** | **bool** | Indicates whether the ledger entry has been deleted or not | [optional] 
**tax_rate** | [**TaxRate**](TaxRate.md) |  | [optional] 
**description** | **str** | The ledger entry description | [optional] 
**journal_code** | [**JournalCode**](JournalCode.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


