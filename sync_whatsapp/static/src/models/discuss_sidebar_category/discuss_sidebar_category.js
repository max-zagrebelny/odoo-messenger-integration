/** @odoo-module **/
import { clear } from "@mail/model/model_field_command";
import { one } from "@mail/model/model_field";
import { registerPatch } from "@mail/model/model_core";

registerPatch({
    name: "DiscussSidebarCategory",
    fields: {
        categoryItemsOrderedByLastAction: {
            compute() {
                if (this.discussAsMLChat_whatsapp) {
                    return this.categoryItems;
                }
                return this._super();
            },
        },
        discussAsMLChat_whatsapp: one("Discuss", {
            identifying: true,
            inverse: "categoryMLChat_whatsapp",
        }),
        isServerOpen: {
            compute() {
                // There is no server state for non-users (guests)
                if (!this.messaging.currentUser) {
                    return clear();
                }
                if (!this.messaging.currentUser.res_users_settings_id) {
                    return clear();
                }
                if (this.discussAsMLChat_whatsapp) {
                    return this.messaging.currentUser.res_users_settings_id
                        .is_discuss_sidebar_category_whatsapp_open;
                }
                return this._super();
            },
        },
        name: {
            compute() {
                if (this.discussAsMLChat_whatsapp) {
                    return this.env._t("Whatsapp");
                }
                return this._super();
            },
        },
        orderedCategoryItems: {
            compute() {
                if (this.discussAsMLChat_whatsapp) {
                    return this.categoryItemsOrderedByLastAction;
                }
                return this._super();
            },
        },
        serverStateKey: {
            compute() {
                if (this.discussAsMLChat_whatsapp) {
                    return "is_discuss_sidebar_category_whatsapp_open";
                }
                return this._super();
            },
        },
        supportedChannelTypes: {
            compute() {
                if (this.discussAsMLChat_whatsapp) {
                    return ["whatsapp"];
                }
                return this._super();
            },
        },
    },
});


