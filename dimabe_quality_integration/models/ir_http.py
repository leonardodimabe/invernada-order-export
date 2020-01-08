from odoo import exceptions, http, models
from odoo.http import request


class ItHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def _auth_method_token():
        # raise exceptions.AccessDenied()
        token = request.httprequest.headers.get('authorization', '', type=str)
        if token:
            token = token.split(' ')[1]
        exceptions._logger.error(token)
        print('')
