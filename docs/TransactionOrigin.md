# TransactionOrigin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**links** | [**list[Link]**](Link.md) | Links for the resource | [optional] 
**due_date** | **date** | The due date of the associated item, e.g. an invoice This attribute is only part of the response when the GET paremeter &#x60;expand_origin&#x3D;true&#x60; is set in the request URL. Even then, it is only available on transaction origins found at the following endpoints: [\&quot;/contact_opening_balance\&quot;, \&quot;/purchase_corrective_invoice\&quot;, \&quot;/sales_corrective_invoice\&quot;, \&quot;/purchase_credit_note\&quot;, \&quot;/purchase_invoice\&quot;, \&quot;/purchase_quick_entry\&quot;, \&quot;/sales_credit_note\&quot;, \&quot;/sales_estimate\&quot;, \&quot;/sales_invoice\&quot;, \&quot;/sales_quick_entry\&quot;, \&quot;/sales_quote\&quot;]. There are other resources, e.g. bank transfers, bank opening balances, or journals, which--though possibly origins of a transaction--can never have this attribute. | [optional] 
**outstanding_amount** | **float** | The outstanding amount of the associated item, e.g. an invoice This attribute is only part of the response when the GET paremeter &#x60;expand_origin&#x3D;true&#x60; is set in the request URL. Even then, it is only available on transaction origins found at the following endpoints: [\&quot;/contact_opening_balance\&quot;, \&quot;/purchase_corrective_invoice\&quot;, \&quot;/sales_corrective_invoice\&quot;, \&quot;/purchase_credit_note\&quot;, \&quot;/purchase_invoice\&quot;, \&quot;/purchase_quick_entry\&quot;, \&quot;/sales_credit_note\&quot;, \&quot;/sales_estimate\&quot;, \&quot;/sales_invoice\&quot;, \&quot;/sales_quick_entry\&quot;, \&quot;/sales_quote\&quot;]. There are other resources, e.g. bank transfers, bank opening balances, or journals, which--though possibly origins of a transaction--can never have this attribute. | [optional] 
**currency** | [**Base**](Base.md) |  | [optional] 
**status** | [**Base**](Base.md) |  | [optional] 
**sent** | **bool** | Indicates whether the associated item, e.g. an invoice, has been sent. This attribute is only present for sales items (not purchase) This attribute is only part of the response when the GET paremeter &#x60;expand_origin&#x3D;true&#x60; is set in the request URL. Even then, it is only available on transaction origins found at the following endpoints: [\&quot;/contact_opening_balance\&quot;, \&quot;/purchase_corrective_invoice\&quot;, \&quot;/sales_corrective_invoice\&quot;, \&quot;/purchase_credit_note\&quot;, \&quot;/purchase_invoice\&quot;, \&quot;/purchase_quick_entry\&quot;, \&quot;/sales_credit_note\&quot;, \&quot;/sales_estimate\&quot;, \&quot;/sales_invoice\&quot;, \&quot;/sales_quick_entry\&quot;, \&quot;/sales_quote\&quot;]. There are other resources, e.g. bank transfers, bank opening balances, or journals, which--though possibly origins of a transaction--can never have this attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


