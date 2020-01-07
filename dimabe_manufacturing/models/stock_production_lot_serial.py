from odoo import fields, models, api


class StockProductionLotSerial(models.Model):
    _inherit = 'stock.production.lot.serial'

    production_id = fields.Many2one(
        'mrp.production',
        'Productión'
    )

    @api.model
    def create(self, values_list):
        res = super(StockProductionLotSerial, self).create(values_list)
        stock_move_line = self.env['stock.move.line'].search([
            ('lot_id', '=', res.stock_production_lot_id.id)
        ])
        raise models.ValidationError(stock_move_line.move_id.production_id.name)
        if production_id:
            res.production_id = production_id.id
        return res

    @api.multi
    def print_serial_label(self):
        return self.env.ref('dimabe_manufacturing.action_stock_production_lot_serial_label_report')\
            .report_action(self)

    @api.multi
    def get_full_url(self):
        self.ensure_one()
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        return base_url
