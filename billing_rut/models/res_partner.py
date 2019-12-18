from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    invoice_rut = fields.Char(
        'Rut Facturación'
    )
