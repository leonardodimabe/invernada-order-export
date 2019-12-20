from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def get_variety(self):
        variety = ''
        if self.is_product_variant:
            variety_variant = self.attribute_value_ids.filtered(
                lambda x: x.attribute_id.name in ['Variedad', 'variedad', 'VARIEDAD']
            )
            if variety_variant:
                variety = variety_variant[0].name

        return variety
