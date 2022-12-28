from odoo import fields, models, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    invoice_id_seq = fields.Many2one(comodel_name='account.move',
                                     compute='get_invoice_number', string='Invoice Number')

    def get_invoice_number(self):
        for item in self:
            sale_order = self.env['sale.order'].search([('name', '=', item.origin)])
            item.invoice_id_seq = False
            if sale_order:
                invoice = self.env['account.move'].search([('invoice_origin', '=', sale_order.name),
                                                           ('state', '!=', 'cancel')], limit=1)
                if invoice:
                    item.invoice_id_seq = invoice.id
