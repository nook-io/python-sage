import pprint
import six
from sage.configuration import Configuration


class PutSalesInvoices(object):
    openapi_types = {"sales_invoice": "PutSalesInvoicesSalesInvoice"}
    attribute_map = {"sales_invoice": "sales_invoice"}

    def __init__(self, sales_invoice=None, local_vars_configuration=None):
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self._sales_invoice = None
        self.discriminator = None
        self.sales_invoice = sales_invoice

    @property
    def sales_invoice(self):
        return self._sales_invoice

    @sales_invoice.setter
    def sales_invoice(self, sales_invoice):
        if (
            self.local_vars_configuration.client_side_validation
            and sales_invoice is None
        ):
            raise ValueError("Invalid value for `sales_invoice`, must not be `None`")
        self._sales_invoice = sales_invoice

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
        if not isinstance(other, PutSalesInvoices):
            return False
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        if not isinstance(other, PutSalesInvoices):
            return True
        return self.to_dict() != other.to_dict()
