# LedgerAccount

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇨🇦, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**ledger_account_group** | [**CoaGroupType**](CoaGroupType.md) |  | [optional] 
**name** | **str** | The name for the ledger account.  Changes to this field do not propagate to other resources, namely not to the name of the associated bank_account (unlike the behaviour of the UI).  | [optional] 
**display_name** | **str** | The display name for the ledger account | [optional] 
**visible_scopes** | **list[str]** | The visible scopes for the ledger account.  This indicates in which of the UI&#39;s areas the ledger account is displayed and available for user selection. Possible entries in this array are &#x60;bank&#x60;, &#x60;sales&#x60;, &#x60;purchasing&#x60;, &#x60;other_payment&#x60;, &#x60;other_receipt&#x60;, &#x60;reporting&#x60;, &#x60;journals&#x60;, &#x60;sales_eu&#x60;, &#x60;sales_row&#x60;, &#x60;purchasing_eu&#x60;, &#x60;purchasing_row&#x60; and &#x60;purchasing_hrc&#x60;.  | [optional] 
**included_in_chart** | **bool** | Indicates whether the ledger account is included in the chart of accounts | [optional] 
**nominal_code** | **int** | The nominal code of the ledger account | [optional] 
**ledger_account_type** | [**Base**](Base.md) |  | [optional] 
**ledger_account_classification** | [**Base**](Base.md) |  | [optional] 
**tax_rate** | [**Base**](Base.md) |  | [optional] 
**fixed_tax_rate** | **bool** | Indicates whether the default tax rate is fixed or may be changed per transaction | [optional] 
**visible_in_banking** | **bool** | Indicates whether the ledger account is displayed in the banking area of the application | [optional] 
**visible_in_expenses** | **bool** | Indicates whether the ledger account is displayed in the purchases area of the application | [optional] 
**visible_in_journals** | **bool** | Indicates whether the ledger account is displayed in the journals area of the application | [optional] 
**visible_in_other_payments** | **bool** | Indicates whether the ledger account is displayed in the other payments area of the application  | [optional] 
**visible_in_other_receipts** | **bool** | Indicates whether the ledger account is displayed in the other receipts area of the application  | [optional] 
**visible_in_reporting** | **bool** | Indicates whether the ledger account is displayed in the reporting area of the application | [optional] 
**visible_in_sales** | **bool** | Indicates whether the ledger account is displayed in the sales area of the application | [optional] 
**balance_details** | [**LedgerAccountBalanceDetails**](LedgerAccountBalanceDetails.md) |  | [optional] 
**is_control_account** | **bool** | Indicates whether the ledger account is a control account.  Control accounts cannot be removed. See also &#x60;control_name&#x60;.  | [optional] 
**control_name** | **str** | The control name for the ledger account.  This is used internally by Accounting to identify the correct ledger account for booking taxes etc. You cannot add ledger accounts with control name and you cannot modify the control name of existing ledger accounts.  | [optional] 
**display_formatted** | **str** | The display name formatted based on coa_list_order in settings | [optional] 
**tax_recoverable** | **bool** | Indicates that transactions posted to this ledger account have part recoverable taxes (Canada only)  | [optional] 
**recoverable_percentage** | **float** | The partial recoverable tax rate (Canada only) | [optional] 
**non_recoverable_ledger_account** | [**LedgerAccount**](LedgerAccount.md) |  | [optional] 
**cis_materials** | **bool** | Indicates whether the ledger account is flagged for CIS Materials | [optional] 
**tax_instalment** | **bool** | Indicates whether the ledger account is flagged for Tax Intalment (Canada only) | [optional] 
**cis_labour** | **bool** | Indicates whether the ledger account is flagged for CIS Labour | [optional] 
**gifi_code** | **int** | The GIFI code of the ledger account.  GIFI is short for The General Index of Financial Information and it lets the CRA validate tax information electronically instead of manually. Information from financial statements is categorized under the appropriate 4-digit-long GIFI code and entered on corporate income tax returns. GIFI is needed when filing a T2 income tax return.  _Canada only_  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


