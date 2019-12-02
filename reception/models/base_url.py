from odoo import models, api


class BaseUrl(models.AbstractModel):
    _name = 'base.url.abstract'

    @api.multi
    def get_full_url(self):
        self.ensure_one()
        base_url = self.env["ir.config_parameter"].get_param("web.base.url")
        return base_url
