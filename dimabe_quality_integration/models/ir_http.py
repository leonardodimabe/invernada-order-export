from odoo import exceptions, http, models
from odoo.http import request


class ItHttp(models.Model):
    _inherit = 'ir.http'

    def _auth_method_token(self):
        # raise exceptions.AccessDenied()
        raise exceptions.AccessError()
        print('')
