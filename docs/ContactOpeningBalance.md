# ContactOpeningBalance

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the areas `Settings`, `Sales`, and `Purchases`: Full Access
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
**contact_opening_balance_type** | [**Base**](Base.md) |  | [optional] 
**contact** | [**Base**](Base.md) |  | [optional] 
**date** | **date** | The date of the opening balance | [optional] 
**reference** | **str** | The reference for the opening balance | [optional] 
**details** | **str** | A description of the opening balance | [optional] 
**net_amount** | **float** | The net amount of the opening balance | [optional] 
**tax_rate** | [**Base**](Base.md) |  | [optional] 
**tax_amount** | **float** | The tax amount of the opening balance | [optional] 
**tax_breakdown** | [**list[TaxBreakdown]**](TaxBreakdown.md) | The tax breakdown for the opening balance | [optional] 
**total_amount** | **float** | The total amount of the opening balance | [optional] 
**currency** | [**Base**](Base.md) |  | [optional] 
**exchange_rate** | **float** | The exchange rate for the opening balance | [optional] 
**base_currency_net_amount** | **float** | The net amount of the opening balance in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the opening balance in base currency | [optional] 
**base_currency_tax_breakdown** | [**list[TaxBreakdown]**](TaxBreakdown.md) | The tax breakdown for the opening balance in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the opening balance in base currency | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


