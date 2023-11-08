from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type_messenger = fields.Selection(string='Type Messenger',
                                      selection=[('none', 'None')],
                                      default='none')

    # @api.model
    # def unlink(self):
    #     channels_records = self.env['mail.channel'].sudo().search([('channel_member_ids', 'in', self.id)])
    #     print(channels_records)
    #     channels_ids = [channel.id for channel in channels_records]
    #     print(channels_ids)
    #     link = self.env['sync.link'].sudo().search([('model', '=', 'mail.channel'), ('ref2', 'in', channels_ids)])
    #     print(link)
    #     for l in link:
    #         l.unlink()
    #     return models.Model.unlink(self)
