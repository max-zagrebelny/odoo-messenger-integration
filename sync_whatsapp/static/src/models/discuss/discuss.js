/** @odoo-module **/

import { one } from "@mail/model/model_field";
import { registerPatch } from "@mail/model/model_core";

registerPatch({
    name: 'Discuss',
    fields: {
        categoryMLChat_whatsapp: one('DiscussSidebarCategory', {
            default: {},
            inverse: 'discussAsMLChat_whatsapp',
         }),
    },
});
