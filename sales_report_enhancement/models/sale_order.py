from odoo import fields, models, api, _


class Order(models.Model):
    _inherit = 'sale.order'

    default_price_list = fields.Many2one(comodel_name='product.pricelist', compute='compute_price_list')

    def compute_price_list(self):
        for item in self:
            item.default_price_list = self.env['product.pricelist'].search([('is_wholesale', '=', True)]).id


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    lot_serial_number_ids = fields.Many2many(comodel_name='stock.lot')
    related_location_id = fields.Many2one(related='order_id.warehouse_id.lot_stock_id')
    product_barcode = fields.Char(related='product_id.barcode')

    @api.onchange('product_id')
    def onchange_product_id(self):
        serials = []
        quants = self.env['stock.quant'].search(
            [('location_id', '=', self.related_location_id.id), ('product_id', '=', self.product_id.id),
             ('location_id.usage', '=', 'internal')])
        for line in quants:
            serials.append(line.lot_id.id)
        return {'domain': {'lot_serial_number_ids': [('product_id', '=', self.product_id.id),
                                                     ('id', 'in', serials), ('product_qty', '!=', 0.0)]}}
