from odoo import api, fields, models



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name_ar = fields.Char('Arabic Name', compute='_calc_name_ar',readonly=True,required=False)
    name_en = fields.Char('Arabic Name', compute='_calc_name_en',readonly=True,required=False)

    @api.depends('name')
    def _calc_name_ar(self):
        env_ar = self.env(context=dict(self._context, lang='ar_SY'))
        for record in self:
            data = env_ar[self._name].browse(record.id).read(['name'])
            print(data)
            if data:
                name_ar = data[0]['name']
                if record.name != name_ar:
                    record.name_ar = name_ar
                else:
                    record.name_ar=False
            else:
                
                record.name_ar = False

    @api.depends('name')
    def _calc_name_en(self):
        env_ar = self.env(context=dict(self._context, lang='en_US'))
        for record in self:
            data = env_ar[self._name].browse(record.id).read(['name'])
            print(data)
            if data:
                name_en = data[0]['name']
                if record.name != name_en:
                    record.name_en = name_en
                else:
                    record.name_en = name_en

            else:

                record.name_en = False


