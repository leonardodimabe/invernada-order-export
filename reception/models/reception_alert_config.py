from odoo import fields, models


class ReceptionAlertConfig(models.Model):
    _name = 'reception.alert.config'

    hr_alert = fields.Float('hr para alerta')

    kg_diff_alert = fields.Float('diferencia de kg para alerta')
