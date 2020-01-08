from odoo import http
from odoo.http import request
from xmlrpc import client


class QualityAnalysis(http.Controller):

    @http.route('/quality_analysis', type='json', auth='user', cors='*')
    def quality_analysis_list(self):
        res = request.env['quality.analysis'].sudo().search([])

        return res.read([
            'pre_caliber',
            'caliber_ids'
        ])

    @http.route('/api/login', type='json', auth='none', cors='*')
    def login(self):
        server_url = 'https://felipecarocadimabe-testerp-dev-792847.dev.odoo.com'
        db_name = 'dev'
        username = 'admin'
        password = 'felipe'
        common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
        user_id = common.authenticate(db_name, username, password, {})
        res = {}
        if user_id:
            res = {
                'user_id': user_id
            }
        else:
            res = {
                'error': 'nop'
            }
        return res

