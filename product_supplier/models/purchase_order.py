from odoo import fields, models, api, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_supplier = fields.Many2one(related='product_id.product_supplier', string='Product Supplier', store=True)
