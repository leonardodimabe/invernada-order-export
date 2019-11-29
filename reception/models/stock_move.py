from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    has_serial_generated = fields.Boolean(
        'tiene series generadas'
    )

    @api.multi
    def generate_serial(self):

        for stock_move in self:
            if stock_move.product_id.tracking == 'serial':
                counter = 1
                for stock_move_line in stock_move.move_line_ids:
                    tmp = '00{}'.format(counter)
                    stock_move_line.lot_name = '{}{}'.format(stock_move.picking_id.name, tmp[-3:])
                    counter += 1
                stock_move.has_serial_generated = True
