# PostSalesQuickEntriesSalesQuickEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quick_entry_type_id** | **str** | The type of quick entry e.g. invoice or credit note | 
**date** | **date** | The date of the quick entry | 
**contact_id** | **str** | The contact the quick entry relates to | 
**reference** | **str** | The reference for the quick entry | 
**ledger_account_id** | **str** | The associated ledger account | 
**contact_name** | **str** | The name of the contact when the quick entry was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the quick entry was created | [optional] 
**details** | **str** | A description of the quick entry | [optional] 
**net_amount** | **float** | The net amount of the quick entry | [optional] 
**tax_rate_id** | **str** | The ID of the Tax Rate. | [optional] 
**tax_amount** | **float** | The tax amount of the quick entry | [optional] 
**total_amount** | **float** | The total amount of the quick entry | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**exchange_rate** | **float** | The exchange rate for the quick entry | [optional] 
**inverse_exchange_rate** | **float** | The inverse exchange rate for the quick entry | [optional] 
**base_currency_net_amount** | **float** | The net amount of the quick entry in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the quick entry in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the quick entry in base currency | [optional] 
**status_id** | **str** | The ID of the Status. | [optional] 
**tax_address_region_id** | **str** | The ID of the Tax Address Region. (Canada only) | [optional] 
**trade_of_asset** | **bool** | Whether the quick entry is marked as trade of asset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


