from odoo import api, models, fields


class SendToEveryone(models.Model):
    _name = "send.to.everyone"
    _description = "Send message to all bot subscribers"

    msg = fields.Text("Message")
    project_id = fields.Many2one("sync.project")
    bot_name = fields.Char('Bot Name', related='project_id.name')

    # sync_partners_ids = fields.Many2many("sync.partner","sync_partner_rel","send_to_everyone_id","sync_partner_id", string='Partners')
    # bot_name = fields.Char('Bot Name', related='project_id.name')
    #
    # @api.depends('project_id')
    # def test(self):
    #     for record in self:
    #         self.write({'sync_partners_ids':record.project_id.user_ids})


class SendToEveryoneViber(models.Model):
    _name = "send.to.everyone.viber"
    _inherit = "send.to.everyone"
    rich_media = fields.Boolean("Rich media")
