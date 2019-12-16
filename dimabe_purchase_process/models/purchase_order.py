from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def get_analytic_accounts(self):
        return self.env['account.analytic.account'].search([])
