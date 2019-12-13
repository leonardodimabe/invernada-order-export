# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': "Reception",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dimabe ltda.",
    'website': "http://www.dimabe.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'purchase_requisition',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
        'mail',
        'purchase_requisition'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/stock_picking.xml',
        'views/res_partner.xml',
        'views/stock_move.xml',
        'views/templates.xml',
        'views/carrier.xml',
        'views/reception_alert_config.xml',
        'reports/reception_label_report.xml',
        'data/alert_config_data.xml',
        'data/reception_notification_mail_template.xml',
        'views/stock_warehouse.xml',
        'views/product_category.xml',
        'views/product_template.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}