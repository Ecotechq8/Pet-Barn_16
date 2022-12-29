{
    "name": "Purchase & Products Enhancement",
    "summary": "Add new object location to use in product object and add some fields in PO and its printout.",
    "version": "15.0.1.0.0",
    "category": "Purchase",
    "author": "Eco-Tech (Omnya Rashwan)",
    "depends": ["base", "stock", "purchase"],
    "data": [
        "security/security_groups.xml",
        "security/ir.model.access.csv",
        "views/product_location_view.xml",
        "views/product_view.xml",
        "views/purchase_order_inh_view.xml",
        "reports/purchase_inh_report_template.xml",
    ],

    "installable": True,
}
