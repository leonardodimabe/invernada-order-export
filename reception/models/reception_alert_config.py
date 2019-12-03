from odoo import fields, models


class ReceptionAlertConfig(models.Model):
    _name = 'reception.alert.config'

    hr_alert = fields.Float('hr para alerta')

    notify_elapsed_time_to = fields.Many2many(
        'res.partner',
        string='Notificar Retraso de Camión a'
    )

    kg_diff_alert = fields.Float('diferencia de kg para alerta')

    notify_diff_kg = fields.Many2many(
        'res.partner',
        string='Notificar Diferencia de kg a'
    )

