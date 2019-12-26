from odoo import fields, models, api


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    def action_next(self):

        raise models.ValidationError(self.move_raw_ids)
        # raise models.ValidationError(self.check_ids)

        res = super(MrpWorkorder, self).action_next()

        raise models.ValidationError(self.move_raw_ids)
        #raise models.ValidationError(self.check_ids)

        return res
