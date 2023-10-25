/** @odoo-module **/

import { registerPatch } from '@mail/model/model_core';
import { clear } from '@mail/model/model_field_command';
import '@mail/models/chatter_topbar';

registerPatch({
    name: 'ChatterTopbar',
    recordMethods: {
        async onClickWhatsapp() {
             let otherFollowers = this.chatter.thread.followers
                    .filter(follower => follower.partner.id !== this.messaging.currentPartner.id);

             if (otherFollowers.length === 0){
                this.messaging.notify({
                    type: 'warning',
                    message: this.env._t("Followers list is empty"),
                });
                return;
             }

             let partners = otherFollowers.map((follower) => follower.partner.id);

             let partnerIds = await this.messaging.rpc({
                model: 'res.partner',
                method: 'search_read',
                kwargs: {
                    domain: [
                         '|',
                        ['parent_id', 'in', partners],
                        ['id', 'in', partners],
                    ],
                },
            });

            let channels = this.messaging.allCurrentClientThreads.map(thread => thread.channel);
            channels = channels.filter((channel) => {
               return channel.channel_type === 'multi_livechat_whatsapp';
            });

            let matchingChannels = channels.filter(channel => {
                return channel.channelMembers.some(member => {
                    return partnerIds.some(partner => partner.id === member.persona.partner.id);
                });
            });

            if (matchingChannels.length === 0) {
                this.messaging.notify({
                    type: 'warning',
                    message: this.env._t("This partner does not have a channel in this messenger"),
                });
                return;
            }
            matchingChannels.forEach(channel => {
                channel.thread.open();
            });
        },
    },
});