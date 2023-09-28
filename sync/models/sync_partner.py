from odoo import api, fields, models, tools
from odoo.exceptions import ValidationError


class SyncPartner(models.Model):
    _name = 'sync.partner'
    _description = 'Union res_partner and sync_link'
    _order = 'id'

    partner_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
    bot_id = fields.Many2one('sync.project', ondelete='cascade', required=True)
    id_user = fields.Integer('ID User', required=True)
    state_user = fields.Char('State', default='None')

    def set_user(self, partner_id, bot_id, id_user):
        existing = self._search_partner(bot_id, id_user)
        if existing:
            # delete_my_code
            print("--- Use existing link ---")
            return existing
        vals = {'partner_id':partner_id,'bot_id':bot_id,'id_user':id_user}
        return self.create(vals)

    def _search_partner(self, bot_id, id_user):
        domain = [('bot_id','=',bot_id),('id_user','=',id_user)]
        return self.search(domain)

    def get_partner(self, bot_id, id_user):
        users = self._search_partner(bot_id, id_user)
        if len(users) > 1:
            raise ValidationError(
                    (
                        "Sync_partner get_user found multiple links"
                    )
                )
        return users.odoo if users else None

    def get_partner_with_create(self, bot_id, id_user, callback_vals, callback_kwargs):
        links = self.get_partner(bot_id, id_user)
        print(links)
        if not links:
            vals = callback_vals(**callback_kwargs)
            print(f"user vals name: {vals['name']}")
            partner = self.env["res.partner"].sudo().create(vals)
            self.set_user(partner.id, bot_id, id_user)
            return partner, True
        return links, False

    @property
    def odoo(self):
        self.ensure_one()
        f = self.env['res.partner'].browse(self.partner_id).id
        return f

    def set_state(self, partner_id, bot_id, state):
        user = self.search([('bot_id', '=', bot_id), ('partner_id', '=', partner_id)])
        user.state_user = state

    def get_state(self, partner_id, bot_id):
        user = self.search([('bot_id', '=', bot_id), ('partner_id', '=', partner_id)])
        return user.state_user

    def _get_eval_context(self):
        return {
            'get_partner':self.get_partner,
            'get_partner_with_create':self.get_partner_with_create,
            'get_state':self.get_state,
            'set_state':self.set_state,
        }