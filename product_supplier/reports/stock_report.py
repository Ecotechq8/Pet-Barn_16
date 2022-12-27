from odoo import fields, models, api, _


class StockReport(models.Model):
    _inherit = "stock.report"

    product_supplier = fields.Many2one(comodel_name='res.partner', string='Supplier')

    def _select(self):
        return super(StockReport, self)._select() + ", sm.product_supplier as product_supplier"

    def _group_by(self):
        return super(StockReport, self)._group_by() + ", sm.product_supplier"
