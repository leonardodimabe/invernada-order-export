# -*- coding: utf-8 -*-
from odoo import http

# class DimabeQualityIntegration(http.Controller):
#     @http.route('/dimabe_quality_integration/dimabe_quality_integration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dimabe_quality_integration/dimabe_quality_integration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dimabe_quality_integration.listing', {
#             'root': '/dimabe_quality_integration/dimabe_quality_integration',
#             'objects': http.request.env['dimabe_quality_integration.dimabe_quality_integration'].search([]),
#         })

#     @http.route('/dimabe_quality_integration/dimabe_quality_integration/objects/<model("dimabe_quality_integration.dimabe_quality_integration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dimabe_quality_integration.object', {
#             'object': obj
#         })