from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    stock_move_line_serial_ids = fields.One2many(
        'stock.move.line.serial',
        'stock_move_line_id'
    )
