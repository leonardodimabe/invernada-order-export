from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    has_serial_generated = fields.Boolean(
        'tiene series generadas',
        compute='_compute_has_serial_generated',
        store=True
    )

    @api.multi
    def _compute_has_serial_generated(self):
        for stock_move in self:
            if len(stock_move.move_line_ids) > 0:
                has_serial = True
                for move_line in stock_move.line_ids:
                    if len(move_line.lot_name) == 0:
                        has_serial = False
                stock_move.has_serial_generated = has_serial
            else:
                stock_move.has_serial_generated = False

    @api.multi
    def generate_serial(self):

        for stock_move in self:
            if stock_move.product_id.tracking == 'serial':
                counter = 1
                for stock_move_line in stock_move.move_line_ids:
                    tmp = '00{}'.format(counter)
                    stock_move_line.lot_name = '{}-{}'.format(stock_move.picking_id.name, tmp[-3:])
                    counter += 1
