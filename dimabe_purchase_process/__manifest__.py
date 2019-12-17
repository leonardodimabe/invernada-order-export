# -*- coding: utf-8 -*-
{
    'name': "Proceso de Compras",

    'summary': """
        proceso de recepción para la invernada""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dimabe ltda",
    'website': "http://www.dimabe.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Solicitud de Compra',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'purchase_requisition',
        'purchase'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/purchase_order.xml',
        'views/purchase_requisition.xml',
        'data/purchase_requisition_mail_template.xml',
        'reports/purchase_order_reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
