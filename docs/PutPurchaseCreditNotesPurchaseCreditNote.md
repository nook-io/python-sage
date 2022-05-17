# PutPurchaseCreditNotesPurchaseCreditNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | The contact the purchase credit note relates to | [optional] 
**date** | **date** | The date of the credit note | [optional] 
**postponed_accounting** | **bool** | Indicates whether postponed accounting rules are applied to the artefact. Only used for UK and IE accounting businesses, where the vendor is flagged as importer | [optional] 
**cis_applicable_amount** | **float** | The total amount of CIS deductible labour - only applicable in UK | [optional] 
**base_currency_cis_applicable_amount** | **float** | The total amount of CIS deductible labour in the base currency - only applicable in UK | [optional] 
**total_after_cis_deduction** | **float** | The total of the artefact with the total of CIS deducted - only applicable in UK | [optional] 
**base_currency_total_after_cis_deduction** | **float** | The total of the artefact with the total of CIS deducted in the base currency - only applicable in UK | [optional] 
**base_currency_total_itc_amount** | **float** | The total amount of input tax credit in base currency for the                      purchase credit note (Canada only) | [optional] 
**total_itc_amount** | **float** | The total amount of input tax credit for the purchase credit note (Canada only) | [optional] 
**base_currency_total_itr_amount** | **float** | The total amount of input tax refund in base currency for the                      purchase credit note (Canada only) | [optional] 
**total_itr_amount** | **float** | The total amount of input tax refund for the purchase credit note (Canada only) | [optional] 
**part_recoverable** | **bool** | Indicates if the purchase credit note is part recoverable or not (Canada only) | [optional] 
**contact_name** | **str** | The name of the contact when the credit note was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the credit note was created | [optional] 
**original_invoice_date** | **date** | The date of the original invoice | [optional] 
**reference** | **str** | The reference for the credit note | [optional] 
**vendor_reference** | **str** | The vendor reference for the credit note | [optional] 
**notes** | **str** | credit note notes | [optional] 
**total_quantity** | **float** | The total quantity of the credit note | [optional] 
**net_amount** | **float** | The net amount of the credit note | [optional] 
**tax_amount** | **float** | The tax amount of the credit note | [optional] 
**total_amount** | **float** | The total amount of the credit note | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**exchange_rate** | **float** | The exchange rate for the credit note | [optional] 
**inverse_exchange_rate** | **str** | The inverse exchange rate for the credit note | [optional] 
**base_currency_net_amount** | **float** | The net amount of the credit note in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the credit note in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the credit note in base currency | [optional] 
**status_id** | **str** | The ID of the Status. | [optional] 
**tax_address_region_id** | **str** | The ID of the Tax Address Region. (Canada only) | [optional] 
**withholding_tax_rate** | **float** | The withheld Tax Rate - only applicable in UK (CIS subcontractor tax rate) | [optional] 
**withholding_tax_amount** | **float** | The withheld Tax Amount - only applicable in UK (CIS subcontractor tax) | [optional] 
**base_currency_withholding_tax_amount** | **float** | The withheld Tax Amount in the base currency - only applicable in UK (CIS subcontractor tax) | [optional] 
**credit_note_lines** | [**list[PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines]**](PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.md) |  | [optional] 
**tax_analysis** | [**list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]**](PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


