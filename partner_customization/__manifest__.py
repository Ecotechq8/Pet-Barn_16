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
            'partner_customization/static/src/js/PartnerDetailsEdit.js',
            'partner_customization/static/src/js/PartnerListScreen.js',
            'partner_customization/static/src/xml/PartnerDetailsEdit.xml',
            'partner_customization/static/src/lib/choices.min.js',

        ]
    },

    "installable": True,
}
