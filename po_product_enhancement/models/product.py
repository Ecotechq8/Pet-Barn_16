from odoo import fields, models, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_location = fields.Many2one(comodel_name='product.location', string='Product Location')


class Product(models.Model):
    _inherit = 'product.product'

    product_location = fields.Many2one(related="product_tmpl_id.product_location", readonly=False)
