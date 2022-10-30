from odoo import fields, models, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand_id = fields.Many2one(related='product_id.brand_id', string='Brand', store=True)

