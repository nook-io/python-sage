import pprint
import six
from sage.configuration import Configuration


class PutInvoiceSettingsInvoiceSettingsDocumentHeadings(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "sales_invoice": "str",
        "sales_credit_note": "str",
        "sales_corrective_invoice": "str",
        "sales_quote": "str",
        "sales_estimate": "str",
        "pro_forma": "str",
        "remittance_advice": "str",
        "statement": "str",
        "delivery_note": "str",
    }
    attribute_map = {
        "sales_invoice": "sales_invoice",
        "sales_credit_note": "sales_credit_note",
        "sales_corrective_invoice": "sales_corrective_invoice",
        "sales_quote": "sales_quote",
        "sales_estimate": "sales_estimate",
        "pro_forma": "pro_forma",
        "remittance_advice": "remittance_advice",
        "statement": "statement",
        "delivery_note": "delivery_note",
    }

    def __init__(
        self,
        sales_invoice=None,
        sales_credit_note=None,
        sales_corrective_invoice=None,
        sales_quote=None,
        sales_estimate=None,
        pro_forma=None,
        remittance_advice=None,
        statement=None,
        delivery_note=None,
        local_vars_configuration=None,
    ):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._sales_invoice = None
        self._sales_credit_note = None
        self._sales_corrective_invoice = None
        self._sales_quote = None
        self._sales_estimate = None
        self._pro_forma = None
        self._remittance_advice = None
        self._statement = None
        self._delivery_note = None
        self.discriminator = None
        if sales_invoice is not None:
            self.sales_invoice = sales_invoice
        if sales_credit_note is not None:
            self.sales_credit_note = sales_credit_note
        if sales_corrective_invoice is not None:
            self.sales_corrective_invoice = sales_corrective_invoice
        if sales_quote is not None:
            self.sales_quote = sales_quote
        if sales_estimate is not None:
            self.sales_estimate = sales_estimate
        if pro_forma is not None:
            self.pro_forma = pro_forma
        if remittance_advice is not None:
            self.remittance_advice = remittance_advice
        if statement is not None:
            self.statement = statement
        if delivery_note is not None:
            self.delivery_note = delivery_note

    @property
    def sales_invoice(self):
        return self._sales_invoice

    @sales_invoice.setter
    def sales_invoice(self, sales_invoice):
        self._sales_invoice = sales_invoice

    @property
    def sales_credit_note(self):
        return self._sales_credit_note

    @sales_credit_note.setter
    def sales_credit_note(self, sales_credit_note):
        self._sales_credit_note = sales_credit_note

    @property
    def sales_corrective_invoice(self):
        return self._sales_corrective_invoice

    @sales_corrective_invoice.setter
    def sales_corrective_invoice(self, sales_corrective_invoice):
        self._sales_corrective_invoice = sales_corrective_invoice

    @property
    def sales_quote(self):
        return self._sales_quote

    @sales_quote.setter
    def sales_quote(self, sales_quote):
        self._sales_quote = sales_quote

    @property
    def sales_estimate(self):
        return self._sales_estimate

    @sales_estimate.setter
    def sales_estimate(self, sales_estimate):
        self._sales_estimate = sales_estimate

    @property
    def pro_forma(self):
        return self._pro_forma

    @pro_forma.setter
    def pro_forma(self, pro_forma):
        self._pro_forma = pro_forma

    @property
    def remittance_advice(self):
        return self._remittance_advice

    @remittance_advice.setter
    def remittance_advice(self, remittance_advice):
        self._remittance_advice = remittance_advice

    @property
    def statement(self):
        return self._statement

    @statement.setter
    def statement(self, statement):
        self._statement = statement

    @property
    def delivery_note(self):
        return self._delivery_note

    @delivery_note.setter
    def delivery_note(self, delivery_note):
        self._delivery_note = delivery_note

    def to_dict(self):
        result = {}
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsDocumentHeadings):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsDocumentHeadings):
            return True
        return self.to_dict() != other.to_dict()
