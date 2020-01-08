from odoo import http
from odoo.http import request


class QualityAnalysis(http.Controller):

    @http.route('/quality_analysis', type='http', auth='none', cors='*')
    def quality_analysis_list(self):
        res = request.env['quality.analysis'].sudo().search([])
        return '<p>lala</p>'
        return res.read([
            'pre_caliber',
            'caliber_ids'
        ])
