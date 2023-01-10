odoo.define('partner_customization.PartnerListScreen', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const { isConnectionError } = require('point_of_sale.utils');

    const { debounce } = require("@web/core/utils/timing");
    const { useListener } = require("@web/core/utils/hooks");
    const PartnerListScreen = require('point_of_sale.PartnerListScreen');

    console.log("YOU ARE HERE ?")
    const PartnerListScreenCustom = (PartnerListScreen) =>
    class extends PartnerListScreen {
          setup() {
            super.setup();
			}


        async saveChanges(event) {
            const CategoryList=$("#inputGroupSelect04").val().map(i=>Number(i));
            const PetsNamesList=$("#pet_names_id").val().map(i=>Number(i));
            event.detail.processedChanges.category_id=CategoryList
            event.detail.processedChanges.pets_names_id=PetsNamesList
            console.log(" event.detail.processedChanges ==", event.detail.processedChanges)
            console.log(" event.detail.processedChanges ==", $("#inputGroupSelect04").val())
            try {
                let partnerId = await this.rpc({
                    model: 'res.partner',
                    method: 'create_from_ui',
                    args: [event.detail.processedChanges],
                });
                await this.env.pos.load_new_partners();
                this.state.selectedPartner = this.env.pos.db.get_partner_by_id(partnerId);
                this.confirm();
            } catch (error) {
                if (isConnectionError(error)) {
                    await this.showPopup('OfflineErrorPopup', {
                        title: this.env._t('Offline'),
                        body: this.env._t('Unable to save changes.'),
                    });
                } else {
                    throw error;
                }
            }
        }
    }


    Registries.Component.extend(PartnerListScreen, PartnerListScreenCustom);


    return PartnerListScreenCustom;
});
