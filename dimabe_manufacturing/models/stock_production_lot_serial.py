from odoo import fields, models, api


class StockProductionLotSerial(models.Model):
    _inherit = 'stock.production.lot.serial'

    @api.multi
    def print_serial_label(self):
        return self.env.ref('dimabe_manufacturing.action_stock_production_lot_serial_label_report')\
            .report_action(self)
