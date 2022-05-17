# OtherPayment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Restricted Access, Full Access
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
**base_currency_total_itc_amount** | **float** | The total amount of input tax credit in base currency for the                      Other Payment (Canada only) | [optional] 
**total_itc_amount** | **float** | The total amount of input tax credit for the Other Payment (Canada only) | [optional] 
**base_currency_total_itr_amount** | **float** | The total amount of input tax refund in base currency for the                      Other Payment (Canada only) | [optional] 
**total_itr_amount** | **float** | The total amount of input tax refund for the Other Payment (Canada only) | [optional] 
**part_recoverable** | **bool** | Indicates if the Other Payment is part recoverable or not (Canada only) | [optional] 
**payment_method** | [**Base**](Base.md) |  | [optional] 
**contact** | [**Base**](Base.md) |  | [optional] 
**bank_account** | [**Base**](Base.md) |  | [optional] 
**tax_address_region** | [**Base**](Base.md) |  | [optional] 
**date** | **date** | The date of the payment | [optional] 
**net_amount** | **float** | The net amount of the payment | [optional] 
**tax_amount** | **float** | The tax amount of the payment | [optional] 
**total_amount** | **float** | The total amount of the payment | [optional] 
**reference** | **str** | A reference of the payment Note: An upper length limit of 25 or 40 characters is imposed conditionally and may not apply in every request. A hard upper limit of 255 characters is imposed by the storage layer, though. | [optional] 
**payment_lines** | [**list[OtherPaymentLineItem]**](OtherPaymentLineItem.md) | The payment lines of the payment | [optional] 
**editable** | **bool** | Indicates whether or not the payment can be edited | [optional] 
**deletable** | **bool** | Indicates whether or not the payment can be deleted | [optional] 
**withholding_tax_rate** | **float** | IRPF withheld tax rate | [optional] 
**withholding_tax_amount** | **float** | IRPF withheld tax amount | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


