/** @odoo-module **/

import { clear } from "@mail/model/model_field_command";
import { one } from "@mail/model/model_field";
import { registerPatch } from "@mail/model/model_core";


registerPatch({
    name: 'DiscussSidebarCategoryItem',
    fields: {
        hasSettingsCommand: {
            compute() {
                return this.channel.channel_type === 'multi_livechat_viber';
            },
        },
        categoryCounterContribution: {
            compute() {
                if (this.channel.channel_type === 'multi_livechat_viber') {
                    return this.channel.localMessageUnreadCounter > 0 ? 1 : 0;
                }
                return this._super();
            },
        },
        counter: {
            compute() {
                if (this.channel.channel_type === 'multi_livechat_viber') {
                    return this.channel.localMessageUnreadCounter;
                }
                return this._super();
            },
        },
        hasUnpinCommand: {
            compute() {
                if (this.channel.channel_type == 'multi_livechat_viber') {
                    return !this.channel.localMessageUnreadCounter;
                }
                return this._super();
            },
        },
    },
});