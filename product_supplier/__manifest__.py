# -*- coding: utf-8 -*-
{
    'name': 'Product Supplier',
    'version': '15.0.1.0.0',
    'category': 'Product',
    'summary': 'Product Supplier',
    'author': 'Eco-Tech, Omnya Rashwan',
    'depends': ['stock', 'sale', 'purchase', 'point_of_sale', 'stock_account', 'stock_enterprise'],
    'data': [
        'views/product_inh_view.xml',
        'views/purchase_report_view.xml',
        'views/sale_report_view.xml',
        'views/stock_report_view.xml',
        'views/pos_report_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

}
