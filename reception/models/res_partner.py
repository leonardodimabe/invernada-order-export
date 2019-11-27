from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sag_code = fields.Char('CSG')

    is_sag_active = fields.Boolean(
        'SAG Activo',
        default=False
    )
