from odoo import models, fields


class StockPicking(models.Model):

    _inherit = "stock.picking"

    multi_approve = fields.Boolean(string="",  )