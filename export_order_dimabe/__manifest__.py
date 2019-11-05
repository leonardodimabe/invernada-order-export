# -*- coding: utf-8 -*-
{
    'name': "export_order_dimabe",

    'summary': """
        Módulo para pedidos de exportación Chile
        """,

    'description': """
        Gestión de pedidos de exportación, con toda la información necesaria.
    """,

    'author': "Dimabe LTDA.",
    'website': "https://www.dimabe.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/custom_port.xml',
        'views/custom_ship.xml',
        'views/custom_shipping_company.xml',
        'views/custom_container_type.xml',
        'views/sale_order.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}