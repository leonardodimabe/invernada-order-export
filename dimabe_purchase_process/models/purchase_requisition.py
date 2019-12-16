from odoo import fields, models, api


class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    @api.model
    def create(self, vals_list):
        if not vals_list['ordering_date']:
            vals_list['ordering_date'] = fields.datetime.now()
        return super(PurchaseRequisition, self).create(vals_list)

    @api.multi
    def action_in_progress(self):
        self.ensure_one()
        template_id = self.env.ref('dimabe_purchase_process.new_requisition_mail_template')
        self.message_post_with_template(template_id.id)
        return super(PurchaseRequisition, self).action_in_progress()

    @api.model
    def get_email_to(self):
        user_group = self.env.ref('dimabe_purchase_process.group_purchase_budget_user')
        email_list = [
            usr.partner_id.email for usr in user_group.users if usr.partner_id.email
        ]
        return ','.join(email_list)
