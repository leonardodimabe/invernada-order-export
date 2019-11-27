from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def button_validate(self):

        raise models.ValidationError(len(self.move_ids_without_package))

        super(StockMoveLine, self).button_validate(self)
