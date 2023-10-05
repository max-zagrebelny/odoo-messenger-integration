from odoo import fields, models


class ResUsersSettings(models.Model):
    _inherit = "res.users.settings"

    is_discuss_sidebar_category_whatsapp_open = fields.Boolean(
        "Is category WhatsApp open", default=True
    )
