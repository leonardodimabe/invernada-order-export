from odoo import fields, models, api


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    stock_production_lot_serial_ids = fields.One2many(
        'stock.production.lot.serial',
        'stock_production_lot_id',
        string="Series"
    )

    @api.multi
    def write(self, values):
        for item in self:
            res = super(StockProductionLot, self).write(values)
            counter = 1
            for serial in item.stock_production_lot_serial_ids:
                counter += counter
                tmp = '00{}'.format(counter)
                serial.serial_number = item.name + tmp[-3:]
            return res
