# -*- coding: utf-8 -*-
from odoo import http
import jwt
import datetime
from xmlrpc import client


@http.route('/api/get_token', type='json', auth='none', cors='*')
def login(self, user, password):
    server_url = 'https://felipecarocadimabe-testerp-dev-792847.dev.odoo.com'
    db_name = 'felipecarocadimabe-testerp-dev-792847'
    common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
    user_id = common.authenticate(db_name, str(user), str(password), {})
    res = {}
    if user_id:
        exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
        payload = {
            'exp': exp,
            'iat': datetime.datetime.utcnow(),
            'sub': user_id,
        }
        token = jwt.encode(
            payload,
            'skjdfe48ueq893rihesdio*($U*WIO$u8',
            algorithm='HS256'
        )
        res = {
            'user_id': user_id,
            'access_token': token
        }
    else:
        res = {
            'error': 'nop'
        }
    return res
