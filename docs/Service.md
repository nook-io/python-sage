# Service

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Restricted Access, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**deletable** | **bool** | Indicates whether the service can be deleted | [optional] 
**deactivatable** | **bool** | Indicates whether the service can be deactivated | [optional] 
**used_on_recurring_invoice** | **bool** | Indicates whether the service has been used on a recurring invoice | [optional] 
**item_code** | **str** | The item code for the service | [optional] 
**description** | **str** | The service description | [optional] 
**notes** | **str** | The notes for the service | [optional] 
**sales_ledger_account** | [**Base**](Base.md) |  | [optional] 
**purchase_ledger_account** | [**Base**](Base.md) |  | [optional] 
**sales_tax_rate** | [**Base**](Base.md) |  | [optional] 
**purchase_tax_rate** | [**Base**](Base.md) |  | [optional] 
**sales_rates** | [**list[Rate]**](Rate.md) | The sales rates for the service | [optional] 
**source_guid** | **str** | Used when importing services from external sources | [optional] 
**purchase_description** | **str** | The service purchase description | [optional] 
**usual_supplier** | [**Contact**](Contact.md) |  | [optional] 
**active** | **bool** | Indicates whether the service is active | [optional] 
**cost_price** | **float** | The cost price of the service | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


