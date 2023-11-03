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


class SendToEveryoneViber(models.Model):
    _name = "send.to.everyone.viber"
    _description = "Send message to all viber bot subscribers"
    _inherit = "send.to.everyone"
    rich_media = fields.Boolean("Carousel")
