from odoo import exceptions, http, models
from odoo.http import request


class ItHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def _auth_method_token():
        # raise exceptions.AccessDenied()
        exceptions._logger.error(request.httprequest.headers.get('authorization', '', type=str))
        print('')
