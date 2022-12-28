from odoo import fields, models, api, _


class ProductLocation(models.Model):
    _name = 'product.location'

    name = fields.Char('Location Name')
