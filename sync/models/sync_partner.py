from odoo import api, fields, models, tools
from odoo.exceptions import ValidationError


class SyncPartner(models.Model):
    _name = 'sync.partner'
    _description = 'Union res_partner and sync_link'
    _order = 'id'

    partner_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
    bot_id = fields.Many2one('sync.project', ondelete='cascade', required=True)
    external_id = fields.Char('ID User', required=True)
    state_user = fields.Char('State', default='None')
    name = fields.Char('Name', related="partner_id.name")

    def set_user(self, partner_id, bot_id, external_id):
        ''' Create new record'''
        existing = self._search_partner(bot_id, external_id)
        if existing:
            return existing
        vals = {'partner_id': partner_id, 'bot_id': bot_id, 'external_id': external_id}
        return self.create(vals)

    def _search_partner(self, bot_id, external_id):
        domain = [('bot_id', '=', bot_id), ('external_id', '=', external_id)]
        return self.search(domain)

    def get_partner(self, bot_id, external_id):
        users = self._search_partner(bot_id, external_id)
        if len(users) > 1:
            raise ValidationError(
                (
                    "Sync_partner get_user found multiple links"
                )
            )
        return users.odoo if users else None

    def get_partner_with_create(self, bot_id, external_id, callback_func=None, callback_kwargs=None):
        ''' If not exist create one'''
        links = self.get_partner(bot_id, external_id)
        if not links and callback_func and callback_kwargs:
            vals = callback_func(**callback_kwargs)
            print(f"user vals name: {vals['name']}")
            partner = self.env["res.partner"].sudo().create(vals)
            self.set_user(partner.id, bot_id, external_id)
            return partner, True
        return links, False

    @property
    def odoo(self):
        self.ensure_one()
        f = self.env['res.partner'].browse(self.partner_id).id
        return f

    def set_state(self, partner_id, bot_id, state):
        print('------------------------')
        user = self.search([('bot_id', '=', bot_id), ('partner_id', '=', partner_id)])
        if not user:
            return
        if user.state_user == 'phone' and state == 'None':
            child_partner = self.env['res.partner'].browse(partner_id)
            print(child_partner)
            partners = self.env['res.partner'].search(
                [('phone', '=', child_partner.phone),('id', '!=', partner_id)])
            print(partners)
            is_parent_exist = False
            parent_part_id = None
            for p in partners:
                if p.parent_id:
                    is_parent_exist = True
                    parent_part_id = p.parent_id
                    break
            if not is_parent_exist:
                list_name = child_partner.name.split(' ')
                list_name.pop()
                name = ''.join(list_name)
                parent_partner = self.env['res.partner'].create({'name': name, 'phone': child_partner.phone})
                parent_part_id = parent_partner.id

            for p in partners:
                p.parent_id = parent_part_id
            child_partner.parent_id = parent_part_id
            # for p in partners:
            #     if not p.parent_id:
            #         child_partner.parent_id = p.id
            #         print(p)
            #         break
        user.state_user = state

    def get_state(self, partner_id, bot_id):
        user = self.search([('bot_id', '=', bot_id), ('partner_id', '=', partner_id)])
        return user.state_user

    def _get_eval_context(self):
        return {
            'get_partner_with_create': self.get_partner_with_create,
            'get_state': self.get_state,
            'set_state': self.set_state,
        }
