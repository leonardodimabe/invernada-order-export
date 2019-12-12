from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    variety_id = fields.Many2one(
        'nut_variety',
        string='Variedad'
    )
