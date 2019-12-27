from odoo import fields, models, api


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    @api.model
    def create(self, values_list):
        res = super(MrpWorkorder, self).create(values_list)

        final_lot = self.env['stock.production.lot'].create({
            'name': self.env['ir.sequence'].next_by_code('mrp.workorder'),
            'product_id': res.product_id.id
        })

        res.final_lot_id = final_lot.id

        return res

    def open_tablet_view(self):
        res = super(MrpWorkorder, self).open_tablet_view()

        for check in self.finished_product_check_ids.filtered(lambda a: a.component_is_byproduct):
            lot_tmp = self.env['stock.production.lot'].create({
                'name': self.env['ir.sequence'].next_by_code('mrp.workorder'),
                'product_id': check.product_id.id
            })
            raise models.ValidationError(len(self.finished_product_check_ids.filtered(lambda a: a.component_is_byproduct)))
            check.lot_id = lot_tmp.id
            self._update_active_move_line()

        return res

    def action_next(self):

        # raise models.ValidationError(self.move_raw_ids)
        # raise models.ValidationError(self.finished_product_check_ids.mapped('component_is_byproduct'))

        res = super(MrpWorkorder, self).action_next()

        # raise models.ValidationError(self.move_raw_ids)
        # raise models.ValidationError(self.check_ids)

        return res
