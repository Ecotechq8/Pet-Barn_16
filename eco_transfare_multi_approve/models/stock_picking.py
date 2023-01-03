from odoo import models, fields
from odoo.exceptions import ValidationError

class StockPicking(models.Model):

    _inherit = "stock.picking"

    multi_approve = fields.Boolean(string="",  )
    active_multi_approve = fields.Boolean(string="",related='picking_type_id.active_multi_approve' )

    def internal_transfare_approval(self):
        for transfare in self:
            if transfare.picking_type_id.active_multi_approve==True:
                if self.picking_type_id.default_location_src_id.owner_id:
                    if self.picking_type_id.default_location_src_id.owner_id.id != self.env.user.id:
                        raise ValidationError(("Cannot Approve the Transfare , please contact with Location Owner"))
                    else:
                        transfare.multi_approve = True
                else:
                    raise ValidationError(("Please Set Owner Location First"))

    def button_validate(self,):
        if self.picking_type_id.active_multi_approve==True:
            if self.picking_type_id.default_location_src_id.owner_id:
                if self.picking_type_id.default_location_src_id.owner_id.id!=self.env.user.id:
                    raise ValidationError(("Cannot Validate the Transfare , please contact with Location Owner"))
                else:
                    if self.multi_approve == False:
                        raise ValidationError(("Please Press To Approve Button First"))
            else:
                raise ValidationError(("Please Set Owner Location First"))


        return super(StockPicking, self).button_validate()