from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def get_analytic_accounts(self):
        res = self.env['account.analytic.account'].search([])
        account_list = []
        tmp = []
        for account in res:
            tmp.append(account)
            if len(tmp) == 2:
                account_list.append(tmp)
                tmp = []
        return account_list

    @api.model
    def get_po_approve_data(self):

        message = self.message_ids.search([('subtype_id', '=', 'SdP aprobada')])
        if message:
            return '{} {}'.format(message.author_id, message.date)
        return ''
