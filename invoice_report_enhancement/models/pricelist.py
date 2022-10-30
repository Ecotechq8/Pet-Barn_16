from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class PriceList(models.Model):
    _inherit = 'product.pricelist'

    is_wholesale = fields.Boolean(string='Wholesale')

    @api.constrains('is_wholesale')
    def check_is_wholesale(self):
        for item in self:
            price_lists = self.env['product.pricelist'].search([('is_wholesale', '=', True),
                                                                ('id', '!=', item.id)])
            if price_lists:
                raise ValidationError(_('There is already wholesale Price List.'))
