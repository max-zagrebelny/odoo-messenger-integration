/** @odoo-module **/

import { clear } from "@mail/model/model_field_command";
import { one } from "@mail/model/model_field";
import { registerPatch } from "@mail/model/model_core";


registerPatch({
    name: 'DiscussSidebarCategoryItem',
    fields: {
        avatarUrl: {
            compute() {
                if (this.channel.channel_type === 'multi_livechat_telegram') {
                    if (this.channel.correspondent) {
                        return this.channel.correspondent.avatarUrl;
                    }
                }
                return this._super();
            },
        },
        categoryCounterContribution: {
            compute() {
                if (this.channel.channel_type === 'multi_livechat_telegram') {
                    return this.channel.localMessageUnreadCounter > 0 ? 1 : 0;
                }
                return this._super();
            },
        },
        counter: {
            compute() {
                if (this.channel.channel_type === 'multi_livechat_telegram') {
                    return this.channel.localMessageUnreadCounter;
                }
                return this._super();
            },
        },
        hasThreadIcon: {
            compute() {
                if (this.channel.channel_type === 'multi_livechat_telegram') {
                    return clear();
                }
                return this._super();
            },
        },
         hasSettingsCommand: {
            compute() {
                return this.channel.channel_type === 'multi_livechat_telegram';
            },
        },
        hasUnpinCommand: {
            compute() {
                if (this.channel.channel_type === 'multi_livechat_telegram') {
                    return !this.channel.localMessageUnreadCounter;
                }
                return this._super();
            },
        },
    },
});