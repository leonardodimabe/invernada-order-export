from odoo import http
from odoo.http import request


class QualityAnalysis(http.Controller):

    @http.route('/quality_analysis', type='json', auth='none')
    def quality_analysis_list(self):
        res = request.env['quality.analysis'].sudo().search([])
        return res.read([
            'caliber_ids'
        ])
