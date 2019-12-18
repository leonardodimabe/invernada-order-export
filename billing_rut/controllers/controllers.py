# -*- coding: utf-8 -*-
from odoo import http

# class BillingRut(http.Controller):
#     @http.route('/billing_rut/billing_rut/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/billing_rut/billing_rut/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('billing_rut.listing', {
#             'root': '/billing_rut/billing_rut',
#             'objects': http.request.env['billing_rut.billing_rut'].search([]),
#         })

#     @http.route('/billing_rut/billing_rut/objects/<model("billing_rut.billing_rut"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('billing_rut.object', {
#             'object': obj
#         })