# -*- coding: utf-8 -*-
import re
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.osv.expression import expression


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    brand_id = fields.Many2one('product.brand', string='Brand')

    def _select(self):
        return super(PurchaseReport, self)._select() + ", l.brand_id as brand_id"

    def _group_by(self):
        return super(PurchaseReport, self)._group_by() + ", l.brand_id"
