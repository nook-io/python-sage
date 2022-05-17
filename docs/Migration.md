# Migration

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the migration | [optional] 
**path** | **str** | The api path for this item | [optional] 
**status** | [**MigrationStatus**](MigrationStatus.md) |  | [optional] 
**started_at** | **datetime** | The date/time the migration started | [optional] 
**completed_at** | **datetime** | The date/time the migration completed | [optional] 
**source_product** | **str** | The source product for the migration | [optional] 
**source_product_version** | **str** | The source product version for the migration | [optional] 
**source_license** | **str** | The source product license for the migration | [optional] 
**source_tool** | **str** | The source product extract tool for the migration | [optional] 
**source_tool_version** | **str** | The source product extract tool version for the migration | [optional] 
**schema_id** | **str** | The schema id used for the migration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


