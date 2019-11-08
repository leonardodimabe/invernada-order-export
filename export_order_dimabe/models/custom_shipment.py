from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CustomShipment(models.Model):
    _name = 'custom.shipment'

    name = fields.Char(
        'Embarque',
        compute='_compute_name'
    )

    shipping_company = fields.Many2one(
        comodel_name='custom.shipping.company',
        string='Naviera'
    )

    ship = fields.Many2one(
        comodel_name='custom.ship',
        string='Nave'
    )

    ship_number = fields.Char(string='Viaje')

    type_transport = fields.Selection(
        selection=[
            ('maritimo', 'Marítimo'),
            ('terrestre', 'Terrestre'),
            ('aereo', 'Aéreo')
        ],
        string='Vía de Transporte'
    )

    departure_port = fields.Many2one(
        comodel_name='custom.port',
        string='Puerto de salida'
    )

    arrival_port = fields.Many2one(
        comodel_name='custom.port',
        string='Puerto de llegada'
    )

    required_loading_date = fields.Date(string='Fecha requerida de carga')

    required_loading_week = fields.Integer(
        'Semana de Carga',
        compute='_compute_required_loading_week',
        store=True
    )

    etd = fields.Date(string='ETD', nullable=True)

    etd_month = fields.Integer(
        'Mes ETD',
        compute='_compute_etd_values',
        store=True
    )

    etd_week = fields.Integer(
        'Semana ETD',
        compute='_compute_etd_values',
        store=True
    )

    eta = fields.Date(string='ETA', nullable=True)

    departure_date = fields.Datetime(string='Fecha de zarpe')

    arrival_date = fields.Datetime(string='Fecha de arribo')

    @api.model
    @api.onchange('etd')
    @api.depends('etd')
    def _compute_etd_values(self):
        if self.etd:
            try:
                self.etd_month = self.etd.month
                _year, _week, _day_of_week = self.etd.isocalendar()
                self.etd_week = _week
            except:
                raise UserWarning('Error producido al intentar obtener el mes y semana de embarque')
        else:
            self.etd_week = None
            self.etd_month = None

    @api.model
    @api.onchange('required_loading_date')
    @api.depends('required_loading_date')
    def _compute_required_loading_week(self):
        if self.required_loading_date:
            try:
                year, week, day_of_week = self.required_loading_date.isocalendar()
                self.required_loading_week = week
            except:
                raise UserWarning('no se pudo establecer la semana de carga')
        else:
            self.required_loading_week = None

    @api.one
    @api.constrains('etd', 'eta')
    def _check_eta_greater_than_etd(self):
        if self.etd == False and self.eta:
            raise ValidationError('Debe ingresar el ETD')
        if self.eta and self.eta < self.etd:
            raise ValidationError('La ETA debe ser mayor al ETD')

    @api.model
    def _compute_name(self):
        self.name = self.shipping_company.name + ' ' + self.ship.name + ' ' + self.ship_number
