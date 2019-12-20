from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def get_variety(self):
        variety = ''
        if self.is_product_variant:
            variety_variant = self.attribute_value_ids
            raise models.ValidationError(variety_variant.attribute_value_id.name)
        return variety
