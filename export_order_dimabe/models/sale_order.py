from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_date = fields.Datetime(string='Fecha de entrega')

    shipping_id = fields.Many2one(
        'custom.shipment',
        'Embarque'
    )

    consignee_id = fields.Many2one(
        'res.partner',
        'Consignatario'
    )

    notify_ids = fields.Many2many(
        'res.partner'
    )

    agent_id = fields.Many2one(
        'res.partner',
        'Agente',
        domain=[('is_agent', '=', True)]
    )

    total_commission = fields.Float(
        'Valor Comisión',
        compute='_compute_total_commission'
    )

    charging_mode = fields.Selection(
        selection=[
            ('piso', 'A Piso'),
            ('slip_sheet', 'Slip Sheet'),
            ('palet', 'Paletizado')
        ],
        string='Modo de Carga')

    booking_number = fields.Char(string='N° Booking')

    bl_number = fields.Char(string='N° BL')

    client_label = fields.Boolean(string='Etiqueta Cliente', default=False)

    container_number = fields.Char(string='N° Contenedor')

    freight_value = fields.Float(string='Valor Flete')

    safe_value = fields.Float(string='Valor Seguro')

    total_value = fields.Float(
        string='Valor Total',
        compute='_compute_total_value',
        store=True
    )

    value_per_kilogram = fields.Float(
        string='Valor por kilo',
        compute='_compute_value_per_kilogram',
        store=True
    )

    remarks = fields.Text(string='Comentarios')

    container_type = fields.Many2one(
        'custom.container.type',
        'Tipo de contenedor'
    )

    @api.model
    @api.depends('freight_value', 'amount_total', 'safe_value')
    def _compute_total_value(self):
        data = self.amount_total - self.freight_value - self.safe_value
        self.total_value = data

    @api.model
    @api.depends('total_value')
    def _compute_value_per_kilogram(self):
        qty_total = 0
        for line in self.order_line:
            qty_total = qty_total + line.product_uom_qty
        if qty_total > 0:
            self.value_per_kilogram = self.total_value / qty_total

    @api.model
    @api.depends('amount_total', 'agent_id')
    def _compute_total_commission(self):
        self.total_commission = (self.agent_id.commission / 100) * self.amount_total
