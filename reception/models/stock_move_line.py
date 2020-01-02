from odoo import fields, models, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    stock_move_line_serial_ids = fields.One2many(
        'stock.move.line.serial',
        'stock_move_line_id'
    )

    @api.model
    def create(self, values_list):
        res = super(StockMoveLine, self).create(values_list)

        prefix = ''
        if res.stock_move_id.product_id.categ_id.is_canning:
            prefix = 'ENV'
        res.lot_name = '{}{}'.format(prefix, res.stock_move_id.picking_id.name)
        res.qty_done = res.product_uom_qty

        return res
