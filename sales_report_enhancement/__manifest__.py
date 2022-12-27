# -*- coding: utf-8 -*-
{
    'name': 'Sales Printout Enhancement',
    'version': '15.0.1.0.0',
    'category': 'Sales',
    'summary': 'modify on invoice printout',
    'author': 'Eco-Tech, Omnya Rashwan',
    'depends': ['base', 'web',
                'sale_management'],
    'data': [
        'reports/custom_sales_report.xml',
        'views/sale_order_inh_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

}
