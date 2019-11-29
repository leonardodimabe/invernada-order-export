from odoo import models, fields


class Carrier(models.Model):

    _name = 'custom.carrier'

    name = fields.Char('Chofer')

    rut = fields.Char('Rut')

    cell_number = fields.Char('Celular')

    truck_patent = fields.Char('Patente Camión')

    cart_patent = fields.Char('Patente Carro')
