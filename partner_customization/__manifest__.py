{
    "name": "Contact Enhancement",
    "summary": "Add Some Helper Fields.",
    "version": "15.0.1.0.0",
    "category": "contact",
    "author": "Elsayed Iraky",
    "depends": ["base","stock","point_of_sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
        "views/pet_product_type.xml",
        "views/product_template.xml",
    ],

    'assets': {
        'point_of_sale.assets': [
            'partner_customization/static/src/js/models.js',
            # 'partner_customization/static/src/xml/bi_pos_stock.xml',
            # 'partner_customization/static/src/lib/jquery.min.js',
            # 'partner_customization/static/src/css/choices.css',
            # 'partner_customization/static/src/lib/choices.min.js',

        ]
    },

    "installable": True,
}
