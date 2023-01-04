from odoo import api, fields, models



class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()
        result['search_params']['fields'].append('category_id')
        result['search_params']['fields'].append('pets_names_id')
        result['search_params']['fields'].append('birthday_date')
        return result


    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result.append('pets.name')
        result.append('res.partner.category')
        print(result)
        return result

    def _get_pos_ui_pets_name(self, params):
        return self.env['pets.name'].search_read(**params['search_params'])

    def _loader_params_pets_name(self):
        return {
            'search_params': {
                'fields': ['id', 'name'],
            },
        }

    def _get_pos_ui_res_partner_category(self, params):
        return self.env['res.partner.category'].search_read(**params['search_params'])

    def _loader_params_res_partner_category(self):
        return {
            'search_params': {
                'domain': [('active', '=', True)],
                'fields': ['id', 'name'],
            },
        }
