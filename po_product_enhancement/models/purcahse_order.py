from odoo import fields, models, api, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_barcode = fields.Char(related='product_id.barcode')
