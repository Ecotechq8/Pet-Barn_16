from odoo import api, fields, models, _


class SaleReport(models.Model):
    _inherit = "sale.report"

    product_supplier = fields.Many2one(comodel_name='res.partner', string='Supplier')

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['product_supplier'] = "l.product_supplier"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            l.product_supplier"""
        return res
