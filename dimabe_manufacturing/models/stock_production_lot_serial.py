from odoo import fields, models, api


class StockProductionLotSerial(models.Model):
    _inherit = 'stock.production.lot.serial'

    @api.multi
    def print_serial_label(self):
        for item in self:
            print(item)
