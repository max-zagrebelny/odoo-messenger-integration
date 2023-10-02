from odoo import api, models, fields


class SendToEveryone(models.Model):
    _name = "send.to.everyone"
    _description = "Send message to all bot subscribers"

    msg = fields.Text("Message")
    project_id = fields.Many2one("sync.project")