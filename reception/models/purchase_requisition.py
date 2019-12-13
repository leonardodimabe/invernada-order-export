from odoo import fields, models, api


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    @api.model
    def create(self, vals_list):
        if 'ordering_date' not in vals_list:
            vals_list['ordering_date'] = fields.datetime.now()
        raise models.ValidationError(fields.datetime.now())
        return super(PurchaseRequisition, self).create(vals_list)
