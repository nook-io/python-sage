# QuickEntry

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access
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
**quick_entry_type** | [**Base**](Base.md) |  | [optional] 
**contact_name** | **str** | The name of the contact when the quick entry was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the quick entry was created | [optional] 
**contact** | [**Base**](Base.md) |  | [optional] 
**date** | **date** | The date of the quick entry | [optional] 
**reference** | **str** | The reference for the quick entry | [optional] 
**ledger_account** | [**Base**](Base.md) |  | [optional] 
**details** | **str** | A description of the quick entry | [optional] 
**net_amount** | **float** | The net amount of the quick entry | [optional] 
**tax_rate** | [**Base**](Base.md) |  | [optional] 
**tax_amount** | **float** | The tax amount of the quick entry | [optional] 
**tax_breakdown** | [**list[TaxBreakdown]**](TaxBreakdown.md) | The tax breakdown for the quick entry | [optional] 
**total_amount** | **float** | The total amount of the quick entry | [optional] 
**outstanding_amount** | **float** | The outstanding amount of the quick entry | [optional] 
**currency** | [**Base**](Base.md) |  | [optional] 
**exchange_rate** | **float** | The exchange rate for the quick entry | [optional] 
**inverse_exchange_rate** | **float** | The inverse exchange rate for the quick entry | [optional] 
**base_currency_net_amount** | **float** | The net amount of the quick entry in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the quick entry in base currency | [optional] 
**base_currency_tax_breakdown** | [**list[TaxBreakdown]**](TaxBreakdown.md) | The tax breakdown for the quick entry in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the quick entry in base currency | [optional] 
**base_currency_outstanding_amount** | **float** | The outstanding amount of the quick entry in base currency | [optional] 
**status** | [**Base**](Base.md) |  | [optional] 
**payments_allocations** | [**list[PaymentAllocation]**](PaymentAllocation.md) | The associated payments and allocations | [optional] 
**tax_address_region** | [**Base**](Base.md) |  | [optional] 
**migrated** | **bool** | Indicates if the quick entry was migrated from another system. | [optional] 
**trade_of_asset** | **bool** | Whether the quick entry is marked as trade of asset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


