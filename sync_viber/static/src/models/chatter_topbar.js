/** @odoo-module **/

import { registerPatch } from '@mail/model/model_core';
import { clear } from '@mail/model/model_field_command';
import '@mail/models/chatter_topbar';

registerPatch({
    name: 'ChatterTopbar',
    recordMethods: {
        async onClickViber() {
             let partners = [];
             let otherFollowers = this.chatter.thread.followers;

             if(this.chatter.thread.suggestedRecipientInfoList) {
                partners = this.chatter.thread.suggestedRecipientInfoList.map((recipient) => recipient.partner)
             }

             partners = partners.concat(otherFollowers.map(follower => follower.partner));
             partners = partners.filter((partner) => {
                return partner.user ? !partner.user.isInternalUser : true;
             });

             if (partners.length === 0){
                this.messaging.notify({
                    type: 'warning',
                    message: this.env._t("The partner is not in the follower list"),
                });
                return;
             }

             partners = partners.map((partner) => partner.id);

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
               return channel.channel_type === 'multi_livechat_viber';
            });

            let matchingChannels = channels.filter(channel => {
                return channel.channelMembers.some(member => {
                    return partnerIds.some(partner => partner.id === member.persona.partner.id);
                });
            });

            if (matchingChannels.length === 0) {
                this.messaging.notify({
                    type: 'warning',
                    message: this.env._t("The partner does not have a channel with this messenger"),
                });
                return;
            }
            matchingChannels.forEach(channel => {
                channel.thread.open();
            });

        },
    },
});