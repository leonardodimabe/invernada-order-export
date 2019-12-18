from odoo import fields, models, api
import re


def format_rut(rut_str):
    raise models.ValidationError(clean_rut(rut_str))
    dv = rut_str[-1:]
    rut_body = rut_str[:-1]

    raise models.ValidationError('{} {}'.format(dv, rut_body))


def clean_rut(rut_str):
    pattern = r'[^0-9kK]/g'
    res = re.sub(pattern, '', rut_str)
    raise models.ValidationError('res {}'.format(res))
    return res


class ResCompany(models.Model):
    _inherit = 'res.company'

    invoice_rut = fields.Char(
        'Rut Facturación'
    )

    @api.model
    def create(self, values_list):
        if 'invoice_rut' in values_list and values_list['invoice_rut']:
            values_list['invoice_rut'] = clean_rut(values_list['invoice_rut'])

        return super(ResCompany, self).create(values_list)

    @api.multi
    def write(self, values):
        if 'invoice_rut' in values and values['invoice_rut']:
            values['invoice_rut'] = clean_rut(values['invoice_rut'])
            raise models.ValidationError(values['invoice_rut'])
        return super(ResCompany, self).write(values)
