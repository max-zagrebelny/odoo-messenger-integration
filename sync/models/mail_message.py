from odoo import api, models, fields


class MailMessage(models.Model):
    _inherit = 'mail.message'

    def action_open_channel(self):
        context = dict(self.env.context)
        context['form_view_initial_mode'] = 'readonly'
        return {
            'type': 'ir.actions.act_window',
            'name': 'Mail Channel Form',
            'res_model': 'mail.channel',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
            'res_id': self.res_id,
            'context': context,
        }