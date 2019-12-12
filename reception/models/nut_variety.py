from odoo import models, fields


class NutVariety(models.Model):
    _name = 'nut.variety'

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'la variedad ya se encuentra en el sistema.')
    ]

    name = fields.Char('Variedad', required=True)