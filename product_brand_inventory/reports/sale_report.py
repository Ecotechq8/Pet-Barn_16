from odoo import api, fields, models, _


class SaleReport(models.Model):
    _inherit = "sale.report"

    brand_id = fields.Many2one('product.brand', string='Brand')

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['brand_id'] = "l.brand_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            l.brand_id"""
        return res
