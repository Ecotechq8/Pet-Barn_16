# -*- coding: utf-8 -*-
{
    'name': 'Product Brand in Inventory',
    'version': '15.0.1.0.0',
    'category': 'Warehouse',
    'summary': 'Product Brand in Inventory',
    'author': 'Eco-Tech, Omnya Rashwan',
    'depends': ['stock', 'sale', 'purchase', 'point_of_sale'],
    'data': [
        'views/brand_views.xml',
        'security/ir.model.access.csv',
        'views/purchase_report_view.xml',
        'views/sale_report_view.xml',
        'views/pos_report_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

}
