# PurchaseInvoice

### Endpoint Availability  * Accounting Plus: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Standard: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Purchases`: Full Access, Restricted Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**links** | [**list[Link]**](Link.md) | Links for the resource | [optional] 
**editable** | **bool** | Indicates whether artefact can be edited | [optional] 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**transaction_type** | [**Base**](Base.md) |  | [optional] 
**postponed_accounting** | **bool** | Indicates whether postponed accounting rules are applied to the artefact. Only used for UK and IE accounting businesses, where the vendor is flagged as importer | [optional] 
**_import** | **bool** | Indicates whether import rules are applied to the artefact. Only used for UK, IE, FR and ES Accounting businesses, where the vendor is flagged as importer. | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**is_cis** | **bool** | Identifies an artefact as CIS (Construction Industry Scheme) applicable - UK only | [optional] 
**cis_applicable_amount** | **float** | The total amount of CIS deductible labour - only applicable in UK | [optional] 
**base_currency_cis_applicable_amount** | **float** | The total amount of CIS deductible labour in the base currency - only applicable in UK | [optional] 
**total_after_cis_deduction** | **float** | The total of the artefact with the total of CIS deducted - only applicable in UK | [optional] 
**base_currency_total_after_cis_deduction** | **float** | The total of the artefact with the total of CIS deducted in the base currency - only applicable in UK | [optional] 
**has_cis_labour** | **bool** | Identifies an artefact as having CIS Labour line items | [optional] 
**has_cis_materials** | **bool** | Identifies an artefact as having CIS Materials line items | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**base_currency_total_itc_amount** | **float** | The total amount of input tax credit in base currency for the                      purchase invoice (Canada only) | [optional] 
**total_itc_amount** | **float** | The total amount of input tax credit for the purchase invoice (Canada only) | [optional] 
**base_currency_total_itr_amount** | **float** | The total amount of input tax refund in base currency for the                      purchase invoice (Canada only) | [optional] 
**total_itr_amount** | **float** | The total amount of input tax refund for the purchase invoice (Canada only) | [optional] 
**part_recoverable** | **bool** | Indicates if the purchase invoice is part recoverable or not (Canada only) | [optional] 
**contact_name** | **str** | The name of the contact when the invoice was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the invoice was created | [optional] 
**date** | **date** | The date of the invoice | [optional] 
**due_date** | **date** | The due date of the invoice | [optional] 
**reference** | **str** | The reference for the invoice | [optional] 
**vendor_reference** | **str** | The vendor reference for the invoice | [optional] 
**notes** | **str** | Invoice notes | [optional] 
**total_quantity** | **float** | The total quantity of the invoice | [optional] 
**net_amount** | **float** | The net amount of the invoice | [optional] 
**tax_amount** | **float** | The tax amount of the invoice | [optional] 
**total_amount** | **float** | The total amount of the invoice | [optional] 
**payments_allocations_total_amount** | **float** | The total amount of all payments and allocations | [optional] 
**payments_allocations_total_discount** | **float** | The total discount of all payments and allocations | [optional] 
**total_paid** | **float** | The total paid amount of the invoice including any payments, allocations and discounts | [optional] 
**outstanding_amount** | **float** | The outstanding amount of the invoice | [optional] 
**currency** | [**Base**](Base.md) |  | [optional] 
**exchange_rate** | **float** | The exchange rate for the invoice | [optional] 
**inverse_exchange_rate** | **float** | The inverse exchange rate for the invoice | [optional] 
**base_currency_net_amount** | **float** | The net amount of the invoice in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the invoice in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the invoice in base currency | [optional] 
**base_currency_outstanding_amount** | **float** | The outstanding amount of the invoice in base currency | [optional] 
**status** | [**Base**](Base.md) |  | [optional] 
**void_reason** | **str** | The reason the invoice was voided | [optional] 
**invoice_lines** | [**list[PurchaseInvoiceLineItem]**](PurchaseInvoiceLineItem.md) | The invoice lines of the invoice | [optional] 
**tax_analysis** | [**list[ArtefactTaxAnalysis]**](ArtefactTaxAnalysis.md) | The invoice tax analysis (Optional for Spain, restricted for all other regions) | [optional] 
**detailed_tax_analysis** | [**ArtefactDetailedTaxAnalysis**](ArtefactDetailedTaxAnalysis.md) |  | [optional] 
**payments_allocations** | [**list[PaymentAllocation]**](PaymentAllocation.md) | The associated payments and allocations | [optional] 
**last_paid** | **date** | The date of the last payment | [optional] 
**tax_address_region** | [**Base**](Base.md) |  | [optional] 
**withholding_tax_rate** | **float** | The withheld Tax Rate - only applicable in UK (CIS subcontractor tax rate) and Spain (IRPF) | [optional] 
**withholding_tax_amount** | **float** | The withheld Tax Amount - only applicable in UK (CIS subcontractor tax) and Spain (IRPF) | [optional] 
**base_currency_withholding_tax_amount** | **float** | The withheld Tax Amount in the base currency - only applicable in UK (CIS subcontractor tax) and Spain (IRPF) | [optional] 
**corrections** | [**list[PurchaseCorrectiveInvoice]**](PurchaseCorrectiveInvoice.md) | The corrective entries associated with the invoice | [optional] 
**tax_reconciled** | **bool** | Indicates if the purchase invoice is tax reconciled or not. | [optional] 
**migrated** | **bool** | Indicates if the purchase invoice was migrated from another system. | [optional] 
**tax_calculation_method** | **str** | The tax calculation method, if applicable, for this purchase invoice, returns invoice or cash. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


