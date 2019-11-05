# -*- coding: utf-8 -*-
from odoo import http

# class ExportOrderDimabe(http.Controller):
#     @http.route('/export_order_dimabe/export_order_dimabe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/export_order_dimabe/export_order_dimabe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('export_order_dimabe.listing', {
#             'root': '/export_order_dimabe/export_order_dimabe',
#             'objects': http.request.env['export_order_dimabe.export_order_dimabe'].search([]),
#         })

#     @http.route('/export_order_dimabe/export_order_dimabe/objects/<model("export_order_dimabe.export_order_dimabe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('export_order_dimabe.object', {
#             'object': obj
#         })