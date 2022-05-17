# Contact

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Restricted Access, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**links** | [**list[Link]**](Link.md) | Links for the resource | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**balance** | **float** | The contact balance | [optional] 
**contact_types** | [**list[Base]**](Base.md) | The type of the contact. It has to be either CUSTOMER or VENDOR | [optional] 
**name** | **str** | The contact&#39;s full name or business name | [optional] 
**reference** | **str** | Unique reference for the contact | [optional] 
**default_sales_ledger_account** | [**LedgerAccount**](LedgerAccount.md) |  | [optional] 
**default_sales_tax_rate** | [**Base**](Base.md) |  | [optional] 
**default_purchase_ledger_account** | [**LedgerAccount**](LedgerAccount.md) |  | [optional] 
**tax_number** | **str** | The VAT registration number of the contact. The format will be validated. | [optional] 
**notes** | **str** | The notes for the contact | [optional] 
**locale** | **str** | The locale for the contact | [optional] 
**main_address** | [**Address**](Address.md) |  | [optional] 
**delivery_address** | [**Address**](Address.md) |  | [optional] 
**main_contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 
**bank_account_details** | [**BankAccountDetails**](BankAccountDetails.md) |  | [optional] 
**credit_limit** | **float** | Custom credit limit amount for the contact &lt;br&gt;&lt;i&gt;not applicable to Start&lt;/i&gt; | [optional] 
**credit_days** | **int** | Custom credit days for the contact.&lt;br&gt; If returned as null in a GET response, you may want to GET /invoice_settings and use &#39;customer_credit_days&#39;/&#39;vendor_credit_days&#39; as default/fallback according to your use case.  | [optional] 
**credit_terms_and_conditions** | **str** | Custom terms and conditions for the contact. If set will override global /invoice_settings default terms and conditions. &lt;br&gt;&lt;i&gt;Customers only&lt;/i&gt;  | [optional] 
**product_sales_price_type** | [**Base**](Base.md) |  | [optional] 
**source_guid** | **str** | Used when importing contacts from external sources | [optional] 
**currency** | [**Base**](Base.md) |  | [optional] 
**aux_reference** | **str** | Auxiliary reference. Used for German \&quot;Kreditorennummer\&quot; and \&quot;Debitorennummer\&quot;. &lt;br&gt; &lt;a href&#x3D;\&quot;https://developer.sage.com/api/accounting/api/settings/#tag/Datev-Settings\&quot;&gt;   See Datev Settings endpoint reference &lt;/a&gt;  | [optional] 
**registered_number** | **str** | The registered number of the contact&#39;s business. Only used for German businesses and represents the \&quot;Steuernummer\&quot; there (not the \&quot;USt-ID\&quot;). | [optional] 
**deletable** | **bool** | Indicates whether the contact can be deleted successfully | [optional] 
**tax_treatment** | [**ContactTaxTreatment**](ContactTaxTreatment.md) |  | [optional] 
**email** | **str** | The email address for the given contact | [optional] 
**tax_calculation** | **str** | &lt;b&gt;France:&lt;/b&gt; The tax calculation method used to define tax treatment &lt;i&gt;Vendors only&lt;/i&gt; &lt;br&gt; &lt;b&gt;Spain:&lt;/b&gt; Defines if contact is a retailer and tax is subject to Recargo de Equivalencia &lt;i&gt;Customers only&lt;/i&gt;  | [optional] 
**auxiliary_account** | **str** | Auxiliary account - used when auxiliary accounting is enabled in business settings. &lt;br&gt;&lt;i&gt;Available only in Spain and France&lt;/i&gt;  | [optional] 
**gdpr_obfuscated** | **bool** | General Data Protection Regulation (GDPR) came into effect on 25th May 2018. It introduces new rules for how business owners manage their contacts&#39; personal data. When this field returns &#39;true&#39;, means that the contact has been requested to be obfuscated and you can not create any artifact (sales invoices, purchase invoices, ...) but you can still check previously created artifacts. | [optional] 
**system** | **bool** | Identifies a contact as being a system contact used for processing specific transaction types and reserved specifically for those transaction types such as tax return payments/refunds. | [optional] 
**has_unfinished_recurring_invoices** | **bool** | Indicates whether the contact is associated with any unfinished recurring invoices | [optional] 
**cis_registered** | **bool** | Identifies a contact as being registered as CIS.&lt;br&gt;&lt;i&gt;only applicable to UK business&lt;/i&gt; | [optional] 
**ni_based** | **bool** | Identifies a contact as being based in Northern Ireland.                   &lt;br&gt;&lt;i&gt;only applicable to UK business&lt;/i&gt; | [optional] 
**cis_settings** | [**ContactCisSettings**](ContactCisSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


