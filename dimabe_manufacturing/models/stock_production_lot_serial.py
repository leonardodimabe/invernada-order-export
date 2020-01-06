from odoo import fields, models, api


class StockProductionLotSerial(models.Model):
    _inherit = 'stock.production.lot.serial'

    @api.multi
    def print_serial_label(self):
        return self.env.ref('dimabe_manufacturing.action_stock_production_lot_serial_label_report')\
            .report_action(self)

    @api.multi
    def get_full_url(self):
        self.ensure_one()
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        return base_url
