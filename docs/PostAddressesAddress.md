# PostAddressesAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_type_id** | **str** | Defines the nature of the address (Shipping, Billing, Head Office etc.).&lt;br&gt;Start defaults to \&quot;Sales\&quot; for Customers and \&quot;Purchasing\&quot; for Vendors | 
**name** | **str** | The custom name of the address | 
**is_main_address** | **bool** | Specifies the address as the contact&#39;s main address. Only a single address can exist for a contact in Start so this is always true when returned by the API but cannot be seen in the UI | 
**address_line_1** | **str** | The first line of the address | [optional] 
**address_line_2** | **str** | The second line of the address | [optional] 
**city** | **str** | The address town/city | [optional] 
**postal_code** | **str** | The address postal code/zipcode | [optional] 
**country_id** | **str** | The ID of the Country. | [optional] 
**bank_account_id** | **str** | The related bank account of the address, if the address belongs to a bank account. | [optional] 
**contact_id** | **str** | The related contact of the address, if the address belongs to a contact. | [optional] 
**region** | **str** | The address state/province/region | [optional] 
**country_group_id** | **str** | The ID of the Country Group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


