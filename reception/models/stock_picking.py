from odoo import models, api, fields

class StockPicking(models.Model):

    _inherit = 'stock.picking'

    guide_number = fields.Integer('Número de Guía')

    weight_guide = fields.Integer('Kilos Guía')

    gross_weight = fields.Integer('Kilos Brutos')

    tare_weight = fields.Integer('Peso Tara')

    net_weight = fields.Integer('Kilos Netos')
