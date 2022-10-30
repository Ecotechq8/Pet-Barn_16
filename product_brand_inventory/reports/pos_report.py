# -*- coding: utf-8 -*-

from functools import partial
from odoo import models, fields


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"

    brand_id = fields.Many2one('product.brand', string='Brand')

    def _select(self):
        return super(PosOrderReport, self)._select() + ', l.brand_id AS brand_id'

    def _group_by(self):
        return super(PosOrderReport, self)._group_by() + ', l.brand_id'
