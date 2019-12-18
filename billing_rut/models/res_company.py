from odoo import fields, models, api
import re


def format_rut(rut_str):
    rut_str = clean_rut(rut_str)
    dv = rut_str[-1:]
    rut_body = rut_str[:-1]
    counter = 0
    formatted_body = ''
    for character in rut_body[::-1]:
        formatted_body += character
        counter += 1
        if counter == 3 and len(formatted_body.replace('.', '')) < len(rut_body):
            counter = 0
            formatted_body += '.'
    raise models.ValidationError('{} {}'.format(formatted_body[::-1], dv))


def clean_rut(rut_str):
    dv = str.upper(rut_str[-1:])
    pattern = r'\D'
    res = re.sub(pattern, '', rut_str)
    return '{}{}'.format(res, dv)


class ResCompany(models.Model):
    _inherit = 'res.company'

    invoice_rut = fields.Char(
        'Rut Facturación'
    )

    @api.model
    def create(self, values_list):
        if 'invoice_rut' in values_list and values_list['invoice_rut']:
            values_list['invoice_rut'] = format_rut(values_list['invoice_rut'])

        return super(ResCompany, self).create(values_list)

    @api.multi
    def write(self, values):
        if 'invoice_rut' in values and values['invoice_rut']:
            values['invoice_rut'] = format_rut(values['invoice_rut'])
            raise models.ValidationError(values['invoice_rut'])
        return super(ResCompany, self).write(values)
