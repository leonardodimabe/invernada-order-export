from odoo import fields, models, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def calculate_done(self):
        stock_traceability_report = self.env['stock.traceability.report'].search([('id', '=', 281)])
        raise models.ValidationError(stock_traceability_report)
        for item in self:
            for line_id in item.finished_move_line_ids:
                line_id.qty_done = line_id.lot_id.total_serial

    @api.multi
    def button_mark_done(self):
        self.calculate_done()
        return super(MrpProduction, self).button_mark_done()

