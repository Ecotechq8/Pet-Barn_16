# -*- coding: utf-8 -*-
{
    'name': 'ECO:POS New Receipt',
    'version': '14.0',
    'summary': """Pos Custom Receipt change odoo POS receipt""",
    'author': "ECo-Tech , Elsayed Iraky",
    'category': 'Point Of Sale',
    'depends': ['point_of_sale'],

    'assets': {
        'point_of_sale.assets': [
            'eco_pos_receipt/static/src/js/**/*',
        ],
        'point_of_sale.assets': [
            'eco_pos_receipt/static/src/xml/**/*',
        ],
    },


}
