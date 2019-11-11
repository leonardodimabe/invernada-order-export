from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_agent = fields.Boolean('Es Agente')

    commission = fields.Float('Comisión')

    @api.constrains('commission')
    def _check_data_typed(self):
        for item in self:
            if item.is_agent and not item.commission or item.commission > 3:
                raise models.ValidationError('la comisión debe ser mayor que 0 y menor o igual que 3')
