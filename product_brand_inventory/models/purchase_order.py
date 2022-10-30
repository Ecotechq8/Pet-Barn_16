from odoo import fields, models, api, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    brand_id = fields.Many2one(related='product_id.brand_id', string='Brand', store=True)

