from odoo import models, api, fields


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    guide_number = fields.Integer('Número de Guía')

    weight_guide = fields.Integer('Kilos Guía')

    gross_weight = fields.Integer('Kilos Brutos')

    tare_weight = fields.Integer('Peso Tara')

    net_weight = fields.Integer('Kilos Netos')

    def button_validate(self):

        for stock_move in self.move_ids_without_package:
            if stock_move.product_id.tracking == 'serial':
                counter = 1
                for stock_move_line in stock_move.move_line_ids:
                    tmp = '00{}'.format(counter)
                    stock_move_line.lot_name = '{}-{}'.format(self.name, tmp[-3])
                    counter += 1
        super(StockPicking, self).button_validate(self)
