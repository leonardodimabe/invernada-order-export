# -*- coding: utf-8 -*-
{
    'name': "Fabricación Dimabe",

    'summary': """
        Módulo que modifica la fabricación actual y la adapta a la realidad de productos frutícolas.
        """,

    'description': "",

    'author': "Dimabe ltda",
    'website': "http://www.dimabe.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'reception',
        'mrp',
        'mrp_workorder'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_workorder.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'views/mrp_workcenter.xml',
        'views/mrp_workorder.xml',
        'views/mrp_workorder.xml'
    ],
}