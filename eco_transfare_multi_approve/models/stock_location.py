# See LICENSE file for full copyright and licensing details.
import json
from odoo import models, fields,api


class StockLocation(models.Model):

    _inherit = "stock.location"


    owner_id_domain = fields.Char(string="",compute="domain_for_user_access", required=False, )
    owner_id = fields.Many2one(comodel_name="res.users", string="Owner ?",domain="owner_id_domain" ,readonly=False, )
    #
    # @api.onchange('name')
    # @api.constrains('name')
    def domain_for_user_access(self):
        for location in self :
            inventory_access_groups = self.env['res.groups'].search([('category_id', '=', 7)])
            location.owner_id_domain=json.dumps([('groups_id', 'in', inventory_access_groups.mapped('id'))])
            print(location.owner_id_domain)


        # self.owner_id=1
        # inventory_access_groups=self.env['res.groups'].search([('category_id','=',7)])
        # # domain = {'foc_sales_order_ids': [('partner_id', '=', self.partner_id.id),
        # #                                   ('state', '=', 'sale'), ('amount_total', '!=', 0.0),
        # #                                   ('is_foc_order', '!=', True)]}
        # # domain= [('groups_id', 'in', inventory_access_groups)]
        # users=self.env['res.users'].search([('groups_id', 'in', inventory_access_groups.mapped('id'))])
        # print(users.mapped('name'))
        # domain = {'owner_id': [('groups_id', 'in', inventory_access_groups.mapped('id'))]}
        # print(domain)
        # return {'domain': domain}
        # # print(users)
        # # return {'domain': users}