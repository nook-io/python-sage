# Address

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Restricted Access, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**address_line_1** | **str** | The first line of the address | [optional] 
**address_line_2** | **str** | The second line of the address | [optional] 
**city** | **str** | The address town/city | [optional] 
**postal_code** | **str** | The address postal code/zipcode | [optional] 
**country** | [**Base**](Base.md) |  | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**bank_account** | [**Base**](Base.md) |  | [optional] 
**contact** | [**Base**](Base.md) |  | [optional] 
**address_type** | [**Base**](Base.md) |  | [optional] 
**name** | **str** | The custom name of the address | [optional] 
**region** | **str** | The address state/province/region | [optional] 
**country_group** | [**Base**](Base.md) |  | [optional] 
**is_main_address** | **bool** | Specifies the address as the contact&#39;s main address. Only a single address can exist for a contact in Start so this is always true when returned by the API but cannot be seen in the UI | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


