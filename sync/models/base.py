# Copyright 2020 Ivan Yelizariev <https://twitter.com/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).

from odoo import models


class Base(models.AbstractModel):
    _inherit = "base"

    # delete_my_code_new
    def set_link(self, relation_name, ref, bot_id, sync_date=None, allow_many2many=False):
        return self.env["sync.link"]._set_link_odoo(
            self, relation_name, ref, bot_id, sync_date, allow_many2many)
    # def set_link(self, relation_name, ref, sync_date=None, allow_many2many=False):
    #     return self.env["sync.link"]._set_link_odoo(
    #         self, relation_name, ref, sync_date, allow_many2many
    #     )

    # delete_my_code_new
    def search_links(self, relation_name, bot_id, refs=None):
        return (
            self.env["sync.link"]
            .with_context(sync_link_odoo_model=self._name)
            ._search_links_odoo(self, relation_name, bot_id, refs))

    # def search_links(self, relation_name, refs=None):
    #     return (
    #         self.env["sync.link"]
    #         .with_context(sync_link_odoo_model=self._name)
    #         ._search_links_odoo(self, relation_name, refs)
    #     )
