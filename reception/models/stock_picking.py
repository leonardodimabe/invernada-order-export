from odoo import models, api, fields


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    guide_number = fields.Integer('Número de Guía')

    weight_guide = fields.Integer('Kilos Guía')

    gross_weight = fields.Integer('Kilos Brutos')

    tare_weight = fields.Integer('Peso Tara')

    net_weight = fields.Integer('Kilos Netos')

    is_mp_reception = fields.Boolean('Recepción de MP')

    sag_code = fields.Char(
        'CSG',
        related='partner_id.sag_code'
    )

    @api.multi
    def action_confirm(self):
        for stock_picking in self:
            if stock_picking.is_mp_reception:
                stock_picking.validate_mp_reception_fields()
            res = super(StockPicking, self).action_confirm()
            if stock_picking.is_mp_reception:
                # stock_moves = self.env['stock.move'].search([('picking_id', '=', stock_picking.id)])
                raise models.ValidationError(stock_picking.move_ids_without_package[0].move_line_ids)

    @api.model
    def validate_mp_reception_fields(self):
        message = ''
        if not self.guide_number:
            message = 'debe agregar número de guía \n'
        if not self.weight_guide:
            message += 'debe agregar kilos guía \n'
        if not self.gross_weight:
            message += 'debe agregar kilos brutos \n'
        if message:
            raise models.ValidationError(message)
