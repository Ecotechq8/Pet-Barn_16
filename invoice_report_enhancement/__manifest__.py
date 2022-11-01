# -*- coding: utf-8 -*-
{
    'name': 'Invoice Printout Enhancement',
    'version': '15.0.1.0.0',
    'category': 'Accounting',
    'summary': 'modify on invoice printout',
    'author': 'Eco-Tech, Omnya Rashwan',
    'depends': ['base', 'web', 'product',
                'account'],
    'data': [
        'views/pricelist_view.xml',
        'reports/custom_invoice_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

}
