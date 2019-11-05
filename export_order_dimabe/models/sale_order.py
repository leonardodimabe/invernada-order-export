from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    departure_port = fields.Many2one(comodel_name='custom.port', string='Puerto de salida')

    arrival_port = fields.Many2one(comodel_name='custom.port', string='Puerto de llegada')

    required_loading_date = fields.Date(string = 'Fecha requerida de carga')

    etd = fields.Date(string='ETD', nullable=True)

    etd_month = fields.Integer(string='Mes ETD', nullable=True, readonly=True)

    etd_week = fields.Integer(string='Semana ETD', nullable=True, readonly=True)

    eta = fields.Date(string='ETA', nullable=True)

    departure_date = fields.Datetime(string='Fecha de zarpe')

    arrival_date = fields.Datetime(string='Fecha de arribo')

    delivery_date = fields.Datetime(string='Fecha de entrega')

    charging_mode = fields.Selection(selection=[('piso', 'A Piso'), ('slip_sheet', 'Slip Sheet'), ('palet', 'Paletizado')], string='Modo de Carga')

    client_label = fields.Boolean(string='Etiqueta Cliente', default=False)

    type_transport = fields.Selection(selection=[('maritimo', 'Marítimo'), ('terrestre', 'Terrestre'), ('aereo', 'Aéreo')], string='Vía de Transporte')

    container_number = fields.Char(string='N° Contenedor')

    booking_number = fields.Char(string='N° Booking')

    bl_number = fields.Char(string='N° BL')

    freight_value = fields.Float(string='Valor Flete')

    safe_value = fields.Float(string='Valor Seguro')

    total_value = fields.Float(string='Valor Total')

    value_per_kilogram = fields.Float(string='Valor por kilo')

    remarks = fields.Text(string='Comentarios')

    container_type = fields.Many2one(comodel_name='custom.container.type', string='Tipo de contenedor')

    shipping_company = fields.Many2one(comodel_name='custom.shipping.company', string='Naviera')

    ship = fields.Many2one(comodel_name='custom.ship', string='Nave')

    ship_number = fields.Char(string='Viaje')

    @api.onchange('etd')
    def set_etd_values(self):
        if self.etd:
            try:
                self.etd_month = self.etd.month
                _year, _week, _day_of_week = self.etd.isocalendar()
                self.etd_week = _week
                print('el mes es {} la semana es {}'.format(self.etd_month, self.etd_week))
            except: 
                raise UserWarning('Error producido al intentar obtener el mes y semana de embarque')
    @api.one
    @api.constrains('etd', 'eta')
    def _check_eta_greater_than_etd(self):
        if self.etd == False and self.eta:
            raise ValidationError('Debe ingresar el ETD')
        if self.eta and self.eta < self.etd:
            raise ValidationError('La ETA debe ser mayor al ETD')
    

    
    