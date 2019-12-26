from odoo import fields, models, api


class StockMoveLineSerial(models.Model):
    _name = 'stock.move.line.serial'

    calculated_weight = fields.Float('Peso Estimado')

    real_weight = fields.Float(
        'Peso Real',
        nulable=True,
        default=None
    )

    stock_move_line_id = fields.Many2one(
        'stock.move.line',
        'Movimiento'
    )

    serial_number = fields.Char(
        'Serie',
        compute='_compute_serial_number',
        store=True
    )

    @api.model
    @api.depends('stock_move_line_id')
    def _compute_serial_number(self):
        self.serial_number = '{}{}'.format(self.stock_move_line_id.lot_name, self.id)
