from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    warehouse_ids = fields.Many2many(
        'stock.warehouse',
        string='Bodegas en las que se puede almacenar'
    )

    is_mp = fields.Boolean(
        'Es MP',
        compute='_compute_is_mp'
    )

    @api.one
    def _compute_is_mp(self):
        if self.parent_id:
            self.is_mp = self.parent_id.name == 'Materia Prima'
        else:
            self.is_mp = self.name == 'Materia Prima'
