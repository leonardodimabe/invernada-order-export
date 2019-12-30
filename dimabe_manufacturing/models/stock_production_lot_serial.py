from odoo import fields, models, api


class StockProductionLotSerial(models.Model):
    _name = 'stock.production.lot.serial'

    calculated_weight = fields.Float('Peso Estimado')

    real_weight = fields.Float(
        'Peso Real',
        nulable=True,
        default=None
    )

    display_weight = fields.Float(
        'Peso',
        compute='_compute_display_weight'
    )

    stock_production_lot_id = fields.Many2one(
        'stock.production.lot',
        'Lote'
    )

    serial_number = fields.Char(
        'Serie'
    )

    @api.model
    def _compute_display_weight(self):
        if self.real_weight:
            self.display_weight = self.real_weight
        else:
            self.display_weight = self.calculated_weight

    @api.model
    def create(self, values_list):

        res = super(StockProductionLotSerial, self).create(values_list)
        counter = 1
        for serial in res.stock_production_lot_serial_ids:
            counter += counter
            tmp = '00{}'.format(counter)
            serial.serial_number = res.stock_production_lot_id.name + tmp[-3:]
        return res
