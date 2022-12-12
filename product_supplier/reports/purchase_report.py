# -*- coding: utf-8 -*-
import re
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.osv.expression import expression


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    product_supplier = fields.Many2one(comodel_name='res.partner', string='Supplier')

    def _select(self):
        return super(PurchaseReport, self)._select() + ", l.product_supplier as product_supplier"

    def _group_by(self):
        return super(PurchaseReport, self)._group_by() + ", l.product_supplier"
