from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = 'stock.move'

    has_serial_generated = fields.Boolean(
        'tiene series generadas'
    )

    product_id = fields.Many2one(
        'product.product',
        'Product',
        domain=lambda self: self._domain_filter(),
        index=True,
        required=True,
        states={'done': [('readonly', True)]}
    )

    products_can_be_stored = fields.Many2many(
        'product.category',
        'productos que pueden ser almacenados',
        related='picking_type_id.warehouse_id.products_can_be_stored'
    )

    def _domain_filter(self):
        domain = [
            ('type', 'in', ['product', 'consu']),
            # ('categ_id', 'in', self.picking_type_id.warehouse_id.products_can_be_stored)
        ]
        _logger.error('aaa {}'.format(self))
        return domain

    @api.multi
    def generate_serial(self):

        for stock_move in self:
            if stock_move.product_id.tracking == 'serial':
                counter = 1
                for stock_move_line in stock_move.move_line_ids:
                    tmp = '00{}'.format(counter)
                    stock_move_line.lot_name = '{}{}'.format(stock_move.picking_id.name, tmp[-3:])
                    stock_move_line.qty_done = stock_move_line.product_uom_qty
                    counter += 1
                stock_move.has_serial_generated = True
