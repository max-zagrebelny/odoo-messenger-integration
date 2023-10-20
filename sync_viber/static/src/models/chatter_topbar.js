/** @odoo-module **/

import { registerPatch } from '@mail/model/model_core';
import { clear } from '@mail/model/model_field_command';
import '@mail/models/chatter_topbar';

registerPatch({
    name: 'ChatterTopbar',
    recordMethods: {
        async onClick() {
          this.chatter.thread.open();
          let otherChannelMembers = this.chatter.thread;
          console.log(otherChannelMembers);
        },
    },
});