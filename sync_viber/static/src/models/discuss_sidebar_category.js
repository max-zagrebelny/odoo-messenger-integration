/** @odoo-module **/

import { clear } from "@mail/model/model_field_command";
import { one } from "@mail/model/model_field";
import { registerPatch } from "@mail/model/model_core";

registerPatch({
    name: "DiscussSidebarCategory",
    fields: {
        categoryItemsOrderedByLastAction: {
            compute() {
                if (this.discussAsMLChat_viber) {
                    return this.categoryItems;
                }
                return this._super();
            },
        },
        discussAsMLChat_viber: one("Discuss", {
            identifying: true,
            inverse: "categoryMLChat_viber",
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
                if (this.discussAsMLChat_viber) {
                    return this.messaging.currentUser.res_users_settings_id
                        .is_discuss_sidebar_category_viber_open
                }
                return this._super();
            },
        },
        name: {
            compute() {
                if (this.discussAsMLChat_viber) {
                    return this.env._t("Viber");
                }
                return this._super();
            },
        },
        orderedCategoryItems: {
            compute() {
                if (this.discussAsMLChat_viber) {
                    return this.categoryItemsOrderedByLastAction;
                }
                return this._super();
            },
        },
        serverStateKey: {
            compute() {
                if (this.discussAsMLChat_viber) {
                    return "is_discuss_sidebar_category_viber_open";
                }
                return this._super();
            },
        },
        supportedChannelTypes: {
            compute() {
                if (this.discussAsMLChat_viber) {
                    return ["viber"];
                }
                return this._super();
            },
        },
    },
});

