# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class PosConfig(models.Model):

    _inherit = "pos.config"

    disable_pricelist_button = fields.Boolean('Hide Price List',default=True)
