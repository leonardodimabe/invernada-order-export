from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    boss_approval_id = fields.Many2one(
        'res.users',
        'vb jefe de área',
        default=None,
        nullable=True
    )

    boss_approval_date = fields.Datetime(
        string='fecha de aprobación jefe',
        default=None,
        nullable=True
    )

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

    @api.multi
    def action_rfq_send(self):
        for item in self:
            # if not item.boss_approval_id:
            item.update({
                'boss_approval_id': self.env.user.id,
                'boss_approval_date': fields.datetime.now()
            })
        return super(PurchaseOrder, self).action_rfq_send()

    @api.model
    def get_po_approve_data(self):

        approve_message = self.message_ids.filtered(lambda x: x.subtype_id.name == 'SdP aprobada')
        if approve_message:
            approve_message = approve_message[0]
            return '{} {}'.format(approve_message.author_id.name, approve_message.date)
        return ''

    @api.model
    def get_mail_sender(self):
        if self.boss_approval_id and self.boss_approval_date:
            raise models.ValidationError(self.boss_approval_id)
            return '{} {}'.format(self.boss_approval_id.name, self.boss_approval_date)
        return ''
