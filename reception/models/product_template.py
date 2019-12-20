from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def get_variety(self):
        variety_variant = self.product_variant_id.attribute_value_ids
        raise models.ValidationError(variety_variant)
