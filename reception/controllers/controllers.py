# -*- coding: utf-8 -*-
from odoo import http

# class Reception(http.Controller):
#     @http.route('/reception/reception/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reception/reception/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reception.listing', {
#             'root': '/reception/reception',
#             'objects': http.request.env['reception.reception'].search([]),
#         })

#     @http.route('/reception/reception/objects/<model("reception.reception"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reception.object', {
#             'object': obj
#         })