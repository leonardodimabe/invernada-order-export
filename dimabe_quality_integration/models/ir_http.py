from odoo import exceptions, http, models
from odoo.http import request
import jwt


class ItHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def _auth_method_token():
        # raise exceptions.AccessDenied()
        token = request.httprequest.headers.get('authorization', '', type=str)
        if token:
            token = token.split(' ')[1]
            a = jwt.decode(token, 'skjdfe48ueq893rihesdio*($U*WIO$u8',algorithms=['HS256'])
            exceptions._logger.error('AAAAA {}'.format(a))
        print('')
