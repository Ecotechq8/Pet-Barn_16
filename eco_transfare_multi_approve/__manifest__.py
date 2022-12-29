# See LICENSE file for full copyright and licensing details.

{
    'name': 'Eco : Transfare Multi Approve',
    'version': '16.0',
    'category': 'Point Of Sale',
    'sequence': 6,
    'summary': 'Multi Approve Picking as per user Selected on Operation Type',
    'author' : 'Elsayed Iraky',
    'description': """

Multi Approve Picking as per user Selected on Operation Type
""",
    'depends': ['stock'],
    'data': [
        'view/stock_location.xml',
        'view/stock_picking_type.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
