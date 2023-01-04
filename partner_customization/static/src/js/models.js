odoo.define('bi_pos_stock.pos', function(require) {
	"use strict";

var { PosGlobalState, Order } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');


const PartnerModels = (PosGlobalState) => class PartnerModels extends PosGlobalState {
    async _processData(loadedData) {
        await super._processData(...arguments);
            this.PetsNames = loadedData['pets.name'];
            this.PartnerCategory = loadedData['res.partner.category'];
    }
}
Registries.Model.extend(PosGlobalState, PartnerModels);
});
