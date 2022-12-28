from odoo import fields, models, api, _
from datetime import datetime


class StockMove(models.Model):
    _inherit = 'stock.move'

    quantity_balance = fields.Float(compute='get_quantity_balance', default=0.0, digits='Product Price',
                                    copy=False)
    product_cost = fields.Monetary(compute='get_quantity_balance', copy=False, string='Unit Cost')
    product_total_cost = fields.Monetary(compute='get_quantity_balance', copy=False, string='Total Cost')
    currency_id = fields.Many2one('res.currency', 'Currency', default=lambda self: self.env.company.currency_id.id)
    sale_price = fields.Monetary(compute='get_quantity_balance', copy=False, string='Sale Price')
    product_uom_qty = fields.Float(
        'Demand',
        digits='Product Price',
        default=1.0, required=True, states={'done': [('readonly', True)]},
        help="This is the quantity of products from an inventory "
             "point of view. For moves in the state 'done', this is the "
             "quantity of products that were actually moved. For other "
             "moves, this is the quantity of product that is planned to "
             "be moved. Lowering this quantity does not generate a "
             "backorder. Changing this quantity on assigned moves affects "
             "the product reservation, and should be done with care.")

    @api.depends('product_id', 'location_id')
    @api.constrains('product_id', 'location_id')
    def get_quantity_balance(self):
        balance_qty = 0.0
        for item in self:
            item.quantity_balance, item.sale_price = 0.0, 0.0
            products = self.env['stock.move'].search([('state', '=', 'done')], order='date asc').mapped('product_id')
            for pro in products:
                if item.product_id == pro:
                    item.product_cost, item.product_total_cost = 0.0, 0.0
                    cost = self.env['stock.valuation.layer'].search([('product_id', '=', item.product_id.id),
                                                                     '|', ('quantity', '=', item.product_uom_qty),
                                                                     ('quantity', '=', -item.product_uom_qty)])
                    if item.location_id.name == 'Inventory adjustment' or item.location_id.name == 'Vendors' or \
                            (item.location_id.name == 'Customers' and item.location_dest_id.name == 'Stock'):
                        balance_qty += item.product_uom_qty
                    elif item.location_dest_id.name == 'Customers' or (
                            item.location_id.name == 'Stock' and item.location_dest_id.name == 'Inventory adjustment') or (
                            item.location_id.name == 'Stock' and (
                            item.location_dest_id.name == 'Customer' or item.location_dest_id.name == 'Scrap' or
                            item.location_dest_id.name == 'Vendors')):
                        balance_qty -= item.product_uom_qty
                        sale_line_price = self.env['sale.order.line'].search([('product_id', '=', item.product_id.id),
                                                                              ('order_id.name', '=',
                                                                               item.origin)], limit=1).price_unit
                        if sale_line_price:
                            item.sale_price = sale_line_price
                    item.quantity_balance = balance_qty
                    for co in cost:
                        if co.time == datetime.strftime(item.date, "%H:%M") and \
                                item.date.date() == co.create_date.date():
                            item.product_cost = co.unit_cost
                            item.product_total_cost = co.value


class StockValuation(models.Model):
    _inherit = 'stock.valuation.layer'

    time = fields.Char(compute='get_time')

    @api.depends('create_date')
    def get_time(self):
        for item in self:
            item.time = False
            if item.create_date:
                item.time = datetime.strftime(item.create_date, "%H:%M")
