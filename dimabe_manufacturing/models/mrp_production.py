from odoo import fields, models, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def calculate_done(self):
        for item in self:
            for line_id in item.finished_move_line_ids:
                raise models.ValidationError(line_id.lot_id.total_serial)
                line_id.qty_done = line_id.lot_id.total_serial

