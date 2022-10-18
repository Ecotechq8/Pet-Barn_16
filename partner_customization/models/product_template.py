from odoo import api, fields, models



class PetProductType(models.Model):
    _name = 'pet.product.type'

    name = fields.Char()



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pet_product_type_id = fields.Many2one(comodel_name="pet.product.type", string="", required=False, )

