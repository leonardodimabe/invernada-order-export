from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    variety_id = fields.Many2one(
        'nut.variety',
        string='Variedad'
    )
