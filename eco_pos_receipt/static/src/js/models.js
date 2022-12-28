odoo.define('eco_pos_receipt.models', function (require) {
"use strict";
    var models = require('point_of_sale.models');
    var core = require('web.core');
    var _t = core._t;

    models.load_fields("res.partner", ["name","barcode"]);

     var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        export_for_printing: function() {
            var json =_super_orderline.export_for_printing.apply(this,arguments);
            json.partner_name =this.get_client().name;
            json.barcode =this.get_client().barcode;
            return json;
        },
    })

    });



