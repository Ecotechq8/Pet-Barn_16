# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details
{
    'name': 'Stock Enhancement',
    'version': '15.0.1.0.0',
    'category': 'Stock',
    'summary': """ ADD NEW FIELDS ON STOCK MOVE TREE VIEW """,
    'description': """ """,
    'sequence': 1,
    'author': 'Eco Tech (Omnya Rashwan)',
    'depends': [
        'stock'
    ],
    'data': [
        'views/stock_move_inh_view.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
