/** @odoo-module **/

import { one } from "@mail/model/model_field";
import { registerPatch } from "@mail/model/model_core";

registerPatch({
    name: 'Discuss',
    fields: {
        categoryMLChat_viber: one('DiscussSidebarCategory', {
            default: {},
            inverse: 'discussAsMLChat_viber',
         }),
    },
});
