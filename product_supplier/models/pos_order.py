from odoo import fields, models, api, _


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    product_supplier = fields.Many2one(related='product_id.product_supplier', string='Product Supplier', store=True)
