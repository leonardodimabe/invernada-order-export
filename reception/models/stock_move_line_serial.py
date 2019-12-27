from odoo import fields, models, api


class StockMoveLineSerial(models.Model):
    _name = 'stock.move.line.serial'

    calculated_weight = fields.Float('Peso Estimado')

    real_weight = fields.Float(
        'Peso Real',
        nulable=True,
        default=None
    )

    display_weight = fields.Float(
        'Peso',
        computed='_compute_display_weight'
    )

    stock_move_line_id = fields.Many2one(
        'stock.move.line',
        'Movimiento'
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
