from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = 'stock.move'

    has_serial_generated = fields.Boolean(
        'tiene series generadas'
    )

    is_mp = fields.Boolean(
        'es mp',
        related='product_id.categ_id.is_mp'
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
            if stock_move.product_id.tracking == 'lot':
                for stock_move_line in stock_move.move_line_ids:
                    prefix = ''
                    if stock_move.product_id.categ_id.is_canning:
                        prefix = 'ENV'
                    stock_move_line.lot_name = '{}{}'.format(prefix, stock_move.picking_id.name)
                    stock_move_line.qty_done = stock_move_line.product_uom_qty
                    if stock_move.product_id.categ_id.is_mp:
                        serials = []
                        total_qty = stock_move.picking_id.get_canning_move().product_uom_qty
                        calculated_weight = stock_move_line.qty_done / total_qty

                        for i in range(total_qty):
                            tmp = '00{}'.format(i)
                            serials.append({
                                'calculated_weight': calculated_weight,
                                'stock_move_line_id': stock_move_line.id,
                                'serial_number': '{}{}'.format(stock_move_line.lot_name, tmp[-3:])
                            })

                        self.env['stock.move.line.serial'].create(serials)

                stock_move.has_serial_generated = True
