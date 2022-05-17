# BusinessSettings

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path for the resource | [optional] 
**siret** | **str** | SIRET Number (France only) | [optional] 
**management_centre_member** | **bool** | Member of Approved Management Centres (France only) | [optional] 
**rcs_number** | **str** | RCS Number (France only) | [optional] 
**share_capital** | **float** | Share Capital (France only) | [optional] 
**business_activity_type** | [**BusinessActivityType**](BusinessActivityType.md) |  | [optional] 
**legal_form_type** | [**LegalFormType**](LegalFormType.md) |  | [optional] 
**auxiliary_accounts_visible** | **bool** | Auxiliary Accounts Visible (France &amp; Spain only) | [optional] 
**default_ledger_accounts** | [**DefaultLedgerAccounts**](DefaultLedgerAccounts.md) |  | [optional] 
**business_type** | [**BusinessType**](BusinessType.md) |  | [optional] 
**country_of_registration** | [**Base**](Base.md) |  | [optional] 
**business_created_at** | **datetime** | The timestamp on which the business was created. This can be the timestamp of the initial creation or the latest business reset. | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


