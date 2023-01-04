# See LICENSE file for full copyright and licensing details.

{
    'name': 'POS Disable PriceList Button',
    'version': '16.0',
    'category': 'Point Of Sale',
    'sequence': 6,
    'summary': 'POS Disable Pricelist Button',
    'author' : 'Elsayed Iraky',
    'description': """

POS Disable Price List Button

""",
    'depends': ['point_of_sale'],
    'data': [
        'view/pos_config.xml',
    ],
    'assets': {
         'point_of_sale.assets': [
            'pos_disable_pricelist_button/static/src/xml/pos_disable_pricelist_button.xml',
            'pos_disable_pricelist_button/static/src/xml/product_card.xml'
        ]
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
