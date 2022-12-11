from odoo import fields, models, api, _


class Order(models.Model):
    _inherit = 'sale.order'

    default_price_list = fields.Many2one(comodel_name='product.pricelist', compute='compute_price_list')

    def compute_price_list(self):
        for item in self:
            item.default_price_list = self.env['product.pricelist'].search([('is_wholesale', '=', True)]).id
