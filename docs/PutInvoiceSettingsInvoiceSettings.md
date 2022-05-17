# PutInvoiceSettingsInvoiceSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_invoice_number** | **int** | The next invoice number | [optional] 
**next_credit_note_number** | **int** | The next credit note number | [optional] 
**separate_invoice_credit_note_numbering** | **bool** | Indicates whether to use separate or combined number sequences for invoices and credit notes | [optional] 
**sales_invoice_number_prefix** | **str** | The prefix to use for sales invoices | [optional] 
**sales_credit_note_number_prefix** | **str** | The prefix to use for sales credit notes | [optional] 
**invoice_terms_and_conditions** | **str** | The default terms and conditions to include on invoices | [optional] 
**default_note_on_invoice** | **str** | The default notes to include on invoices | [optional] 
**default_note_on_credit_note** | **str** | The default notes to include on credit notes | [optional] 
**next_quote_number** | **int** | The next quote number | [optional] 
**quote_number_prefix** | **str** | The prefix to use for sales quotes | [optional] 
**estimate_number_prefix** | **str** | The prefix to use for sales estimates | [optional] 
**quote_default_days_to_expiry** | **int** | The default number of days before quotes expire | [optional] 
**estimate_default_days_to_expiry** | **int** | The default number of days before estimates expire | [optional] 
**quote_terms_and_conditions** | **str** | The default terms and conditions to include on quotes | [optional] 
**estimate_terms_and_conditions** | **str** | The default terms and conditions to include on estimates | [optional] 
**delivery_note_terms_and_conditions** | **str** | The default terms and conditions to include on delivery notes | [optional] 
**delivery_note_show_signature** | **bool** | Indicates whether to include the signature lines on delivery notes | [optional] 
**delivery_note_show_picked** | **bool** | Indicates whether to include the picked column on delivery notes | [optional] 
**delivery_note_show_notes** | **bool** | Indicates whether to include the document notes on delivery notes | [optional] 
**delivery_note_show_contact_details** | **bool** | Indicates whether to include contact details on delivery notes | [optional] 
**quick_entry_prefix** | **str** | The prefix to use for quick entries | [optional] 
**late_payment_percentage** | **float** | The percentage charge applied to late payment of invoices (France only) | [optional] 
**prompt_payment_percentage** | **float** | The percentage applied to late payment of invoices (France only) | [optional] 
**show_auto_entrepreneur** | **bool** | Indicates whether to include auto entrepreneur details on invoices (France only) | [optional] 
**show_insurance** | **bool** | Indicates whether to include insurance details on invoices (France only) | [optional] 
**insurer_id** | **str** | The ID of the Insurer. (France only) | [optional] 
**insurance_area** | **str** | The insurance area to be displayed on invoices (France only) | [optional] 
**insurance_type** | **str** | The insurance type to be displayed on invoices (France only) | [optional] 
**insurance_text** | **str** | The insurance mention to be displayed on invoices (France only) | [optional] 
**payment_bank_account_id** | **str** | The ID of the Payment Bank Account. | [optional] 
**sales_corrective_invoice_number_prefix** | **str** | The sales corrective invoice number prefix (Spain only) | [optional] 
**next_sales_corrective_invoice_number** | **int** | The next sales corrective invoice number | [optional] 
**customer_credit_days** | **int** | The default delay within which the business&#39; customer has to pay an invoice Prefer the (customer) contact&#39;s attribute &#39;credit_days&#39; over this setting to calculate an invoice&#39;s date of payment; only if null, use this as default.  | [optional] 
**vendor_credit_days** | **int** | The default delay within which the business has to pay any vendor&#39;s invoice Prefer the specific (vendor) contact&#39;s attribute &#39;credit_days&#39; over this setting; only if null, use this as default.  | [optional] 
**document_headings** | [**PutInvoiceSettingsInvoiceSettingsDocumentHeadings**](PutInvoiceSettingsInvoiceSettingsDocumentHeadings.md) |  | [optional] 
**line_item_titles** | [**PutInvoiceSettingsInvoiceSettingsLineItemTitles**](PutInvoiceSettingsInvoiceSettingsLineItemTitles.md) |  | [optional] 
**footer_details** | [**PutInvoiceSettingsInvoiceSettingsFooterDetails**](PutInvoiceSettingsInvoiceSettingsFooterDetails.md) |  | [optional] 
**print_contact_details** | [**PutInvoiceSettingsInvoiceSettingsPrintContactDetails**](PutInvoiceSettingsInvoiceSettingsPrintContactDetails.md) |  | [optional] 
**print_statements** | [**PutInvoiceSettingsInvoiceSettingsPrintStatements**](PutInvoiceSettingsInvoiceSettingsPrintStatements.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


