from odoo import fields, models, api, _


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    brand_id = fields.Many2one(related='product_id.brand_id', string='Brand', store=True)


