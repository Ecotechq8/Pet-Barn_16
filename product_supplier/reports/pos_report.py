# -*- coding: utf-8 -*-

from functools import partial
from odoo import models, fields


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"

    product_supplier = fields.Many2one(comodel_name='res.partner', string='Supplier')

    def _select(self):
        return super(PosOrderReport, self)._select() + ', l.product_supplier AS product_supplier'

    def _group_by(self):
        return super(PosOrderReport, self)._group_by() + ', l.product_supplier'
