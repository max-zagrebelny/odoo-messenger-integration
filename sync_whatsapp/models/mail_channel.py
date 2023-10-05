from odoo import fields, models


class MailChannel(models.Model):
    _inherit = "mail.channel"

    channel_type = fields.Selection(
        selection_add=[("multi_livechat_whatsapp", "WhatsApp")],
        ondelete={"multi_livechat_whatsapp": "cascade"},
    )
