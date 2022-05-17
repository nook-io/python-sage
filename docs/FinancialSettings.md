# FinancialSettings

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The api path for this item | [optional] 
**year_end_date** | **date** | The financial year end date of the business | [optional] 
**year_end_lockdown_date** | **date** | The year end lockdown date of the business | [optional] 
**accounting_type** | **str** | Indicates the accounting type of a business, it can be accrual or cash based | [optional] 
**accounts_start_date** | **date** | The accounts start date of the business | [optional] 
**base_currency** | [**Base**](Base.md) |  | [optional] 
**multi_currency_enabled** | **bool** | Indicates whether multi-currency is enabled for the business | [optional] 
**use_live_exchange_rates** | **bool** | Indicates whether to use live or business defined exchange rates | [optional] 
**mtd_activation_status** | **str** | Indicates the UK Making Tax Digital for VAT activation status | [optional] 
**mtd_connected** | **bool** | Indicates whether UK Making Tax Digital for VAT is currently connected | [optional] 
**mtd_authenticated_date** | **date** | Indicates when a UK business enabled UK Making Tax Digital for VAT, nil if not enabled or non-uk | [optional] 
**tax_scheme** | [**TaxScheme**](TaxScheme.md) |  | [optional] 
**tax_return_frequency** | [**Base**](Base.md) |  | [optional] 
**tax_number** | **str** | The tax number | [optional] 
**general_tax_number** | **str** | The number for various tax report submissions | [optional] 
**tax_office** | [**Base**](Base.md) |  | [optional] 
**default_irpf_rate** | **float** | The default IRPF rate | [optional] 
**flat_rate_tax_percentage** | **float** | The tax percentage that applies to flat rate tax schemes. | [optional] 
**recoverable_percentage** | **float** | The partial recoverable tax rate (Canada only) | [optional] 
**sales_tax_calculation** | **str** | The method of collection for tax on sales. Allowed values - \&quot;invoice\&quot;, \&quot;cash\&quot;. | [optional] 
**purchase_tax_calculation** | **str** | The method of collection for tax on purchases. Allowed values - \&quot;invoice\&quot;, \&quot;cash\&quot;. | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


