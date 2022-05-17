# ContactPerson

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Restricted Access, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**contact_person_types** | [**list[ContactPersonType]**](ContactPersonType.md) | The contact person types for the contact person. Get possible types by retrieving &lt;a href&#x3D;\&quot;https://developer.sage.com/api/accounting/api/contacts/#operation/getContactPersonTypes\&quot;&gt;   all available contact person types &lt;/a&gt;.  | [optional] 
**name** | **str** | The name of the contact person | [optional] 
**job_title** | **str** | The job title of the contact person | [optional] 
**telephone** | **str** | The telephone number of the contact person | [optional] 
**mobile** | **str** | The mobile number of the contact person | [optional] 
**email** | **str** | The email address of the contact person | [optional] 
**fax** | **str** | The fax number of the contact person | [optional] 
**is_main_contact** | **bool** | Indicates whether this is the main contact person. Per contact, only one main contact can be selected. | [optional] 
**address** | [**Base**](Base.md) |  | [optional] 
**is_preferred_contact** | **bool** | Indicates whether this contact person is a preferred contact | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


