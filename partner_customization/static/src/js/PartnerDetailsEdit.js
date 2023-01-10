odoo.define('partner_customization.PartnerDetailsEdit', function(require) {
    'use strict';

    const { _t } = require('web.core');
    const { getDataURLFromFile } = require('web.utils');
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const PartnerDetailsEdit = require('point_of_sale.PartnerDetailsEdit');
    const { onMounted, onWillUnmount } = owl;

    console.log("YOU ARE HERE ?")
    const PartnerDetailsEditCustom = (PartnerDetailsEdit) =>
    class extends PartnerDetailsEdit {
        setup() {
            super.setup();


            $(document).ready(function(){
                 var multipleSelectDropdown = new Choices('#inputGroupSelect04', {
                    removeItemButton: false,
                  });
                  var PetNameDropdown = new Choices('#pet_names_id', {
                    removeItemButton: false
                  });
            });
        }

    }


    Registries.Component.extend(PartnerDetailsEdit, PartnerDetailsEditCustom);


    return PartnerDetailsEditCustom;
});
