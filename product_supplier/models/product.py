from odoo import fields, models, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_supplier = fields.Many2one(comodel_name='res.partner', string='Supplier',
                                       domain="[('supplier_rank', '!=', 0)]")


class Product(models.Model):
    _inherit = 'product.product'

    product_supplier = fields.Many2one(related='product_tmpl_id.product_supplier', string='Supplier',
                                       readonly=False, domain="[('supplier_rank', '!=', 0)]")


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    product_supplier = fields.Many2one(related='product_id.product_supplier')


class StockMove(models.Model):
    _inherit = 'stock.move'

    product_supplier = fields.Many2one(related='product_id.product_supplier', store=True)


class StockValuation(models.Model):
    _inherit = 'stock.valuation.layer'

    product_supplier = fields.Many2one(related='product_id.product_supplier')
