# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': "Proceso de Compras",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dimabe ltda",
    'website': "http://www.dimabe.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Solicitud de Compra',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'purchase_requisition',
        'purchase'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/groups.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/purchase_order.xml',
        'views/purchase_requisition.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}