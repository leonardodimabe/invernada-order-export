from odoo import fields, models, api


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    def do_finish(self):

        # raise models.ValidationError(self.move_raw_ids)
        # raise models.ValidationError(self.finished_product_check_ids)

        res = super(MrpWorkorder, self).do_finish()

        # raise models.ValidationError(self.move_raw_ids)
        # raise models.ValidationError(self.check_ids)

        return res