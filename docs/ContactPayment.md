# ContactPayment

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Restricted Access, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**links** | [**list[Link]**](Link.md) | Links for the resource | [optional] 
**transaction** | [**Base**](Base.md) |  | [optional] 
**transaction_type** | [**Base**](Base.md) |  | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**payment_method** | [**Base**](Base.md) |  | [optional] 
**contact** | [**Base**](Base.md) |  | [optional] 
**bank_account** | [**Base**](Base.md) |  | [optional] 
**date** | **date** | The date the payment was made | [optional] 
**net_amount** | **float** | The net amount of the payment | [optional] 
**tax_amount** | **float** | The tax amount of the payment | [optional] 
**total_amount** | **float** | The total amount of the payment | [optional] 
**currency** | [**Base**](Base.md) |  | [optional] 
**exchange_rate** | **float** | The exchange rate of the payment | [optional] 
**base_currency_net_amount** | **float** | The net amount of the payment in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the payment in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the payment in base currency | [optional] 
**base_currency_currency_charge** | **float** | The currency conversion charges in base currency | [optional] 
**reference** | **str** | A reference for the payment Note: An upper length limit of 25 or 40 characters is imposed conditionally and may not apply in every request. A hard upper limit of 255 characters is imposed by the storage layer, though. | [optional] 
**allocated_artefacts** | [**list[AllocatedPaymentArtefact]**](AllocatedPaymentArtefact.md) | The allocated artefacts | [optional] 
**tax_rate** | [**Base**](Base.md) |  | [optional] 
**payment_on_account** | [**PaymentOnAccount**](PaymentOnAccount.md) |  | [optional] 
**editable** | **bool** | Indicates whether payment can be edited | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


