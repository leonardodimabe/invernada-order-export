from odoo import models, api, fields


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    guide_number = fields.Integer('Número de Guía')

    weight_guide = fields.Integer('Kilos Guía')

    gross_weight = fields.Integer('Kilos Brutos')

    tare_weight = fields.Integer('Peso Tara')

    net_weight = fields.Integer('Kilos Netos')

    is_mp_reception = fields.Boolean('Recepción de MP')

    carrier_id = fields.Many2one('custom.carrier', 'Conductor')

    carrier_rut = fields.Char(
        'Rut',
        related='carrier_id.rut'
    )

    carrier_cell_phone = fields.Char(
        'Celular',
        related='carrier_id.cell_number'
    )

    carrier_truck_patent = fields.Char(
        'Patente Camión',
        related='carrier_id.truck_patent'
    )

    carrier_cart_patent = fields.Char(
        'Patente Carro',
        related='carrier_id.cart_patent'
    )

    sag_code = fields.Char(
        'CSG',
        related='partner_id.sag_code'
    )

    @api.model
    def get_mp_move(self):
        return self.move_ids_without_package.filtered(lambda x: x.has_tracking == 'serial')

    @api.model
    def get_canning_move(self):
        return self.move_ids_without_package.filtered(lambda x: x.has_tracking != 'serial')

    @api.multi
    def action_confirm(self):
        for stock_picking in self:
            if stock_picking.is_mp_reception:
                stock_picking.validate_mp_reception()
            res = super(StockPicking, self).action_confirm()
            if stock_picking.is_mp_reception:

                mp = stock_picking.get_mp_move()
                if len(mp) != 1:
                    raise models.ValidationError('No se encontró materia prima en las operaciones')
                canning = stock_picking.get_canning_move()
                if len(canning) != 1:
                    raise models.ValidationError('no se encontró registro de envases en las operaciones')

                total_canning = canning.product_uom_qty
                unit_weight = mp.product_uom_qty / total_canning

                counter = 0
                for move_line in mp.move_line_ids:
                    move_line.product_uom_qty = unit_weight
                    if counter >= total_canning:
                        move_line.unlink()
                    counter += 1

            return res

    @api.model
    def validate_mp_reception(self):
        message = ''
        if not self.guide_number:
            message = 'debe agregar número de guía \n'
        if not self.weight_guide:
            message += 'debe agregar kilos guía \n'
        if not self.gross_weight:
            message += 'debe agregar kilos brutos \n'

        if len(self.move_ids_without_package) != 2:
            message += 'debe agregar MP y envases al listado de operaciones'
        if message:
            raise models.ValidationError(message)

    @api.multi
    def get_full_url(self):
        self.ensure_one()
        base_url = self.env["ir.config_parameter"].get_param("web.base.url")
        return base_url
