from odoo import fields, models, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    default_price_list = fields.Many2one(comodel_name='product.pricelist', compute='compute_price_list')

    def compute_price_list(self):
        for item in self:
            item.default_price_list = self.env['product.pricelist'].search([('is_wholesale', '=', True)]).id


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    expiration_date = fields.Char(compute="get_expiration_date")

    def get_expiration_date(self):
        for item in self:
            item.expiration_date = False
            if item.sale_line_ids.order_id.picking_ids:
                print('ddddddddddddddddddd')
                for pic in item.sale_line_ids.order_id.picking_ids:
                    print(pic)
                    for line in pic.move_line_ids_without_package:
                        if line.product_id == item.product_id and line.lot_id:
                            print(line.lot_id.expiration_date)
                            item.expiration_date = str(line.lot_id.expiration_date.date())
