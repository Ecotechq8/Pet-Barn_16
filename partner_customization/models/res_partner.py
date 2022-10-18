from odoo import fields, models, api, _




class PetsName(models.Model):
    _name = 'pets.name'

    name = fields.Char()
    color = fields.Integer(string="", required=False, )


class ResPartner(models.Model):
    _inherit = 'res.partner'

    pets_names_id = fields.Many2many(comodel_name="pets.name", relation="name",string="Pets Name", )
    birthday_date = fields.Date(string="", required=False, )