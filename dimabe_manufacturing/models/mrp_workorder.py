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

    def action_next(self):

        # raise models.ValidationError(self.move_raw_ids)
        # raise models.ValidationError(self.finished_product_check_ids)

        res = super(MrpWorkorder, self).action_next()

        # raise models.ValidationError(self.move_raw_ids)
        # raise models.ValidationError(self.check_ids)

        return res
