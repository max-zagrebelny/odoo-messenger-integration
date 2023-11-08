from odoo import api, models, fields


class SendToEveryone(models.Model):
    _name = "send.to.everyone"
    _description = "Send message to all bot subscribers"

    msg = fields.Text("Message")
    image = fields.Binary("Image")
    link = fields.Char("Add link")
    link_text = fields.Char("Link text")
    project_id = fields.Many2one("sync.project")
    url = fields.Char("Image url")
    bot_name = fields.Char('Bot Name', related='project_id.name')
    # bot_type = fields.Char('Bot type', related="project_id.eval_context_ids.name")
    bot_type = fields.Char('Bot type')
    rich_media = fields.Boolean("Carousel", default=False)

    def action_open_send_to_everyone(self):
        context = dict(self.env.context)
        context['form_view_initial_mode'] = 'readonly'
        return {
            'type': 'ir.actions.act_window',
            'name': 'Send to everyone Form',
            'res_model': 'send.to.everyone',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
            'res_id': self.id,
            'context': context,
        }


