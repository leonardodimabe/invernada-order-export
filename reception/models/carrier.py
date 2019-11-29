from odoo import models, fields, api


class Carrier(models.Model):

    _name = 'custom.carrier'

    name = fields.Char(
        'Conductor',
        required=True
    )

    rut = fields.Char(
        'Rut',
        required=True
    )

    cell_number = fields.Char('Celular')

    truck_patent = fields.Char('Patente Camión')

    cart_patent = fields.Char('Patente Carro')

    @api.model
    def create(self, values_list):
        if 'truck_patent' in values_list:
            values_list['truck_patent'] = str.upper(values_list['truck_patent'])

        return super(Carrier, self).create(values_list)

    @api.multi
    def write(self, vals):
        if 'truck_patent' in vals:
            vals['truck_patent'] = str.upper(vals['truck_patent'])
        if 'cart_patent' in vals:
            vals['cart_patent'] = str.upper(vals['cart_patent'])

        return super(Carrier, self).write(vals)
