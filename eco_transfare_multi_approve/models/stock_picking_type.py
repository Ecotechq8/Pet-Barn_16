from odoo import api, fields, models




class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    active_multi_approve = fields.Boolean(string="Multi Aprrove ? ",  )
