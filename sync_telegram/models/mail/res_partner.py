from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type_messenger = fields.Selection(string='Type Messenger',
                                      selection_add=[('telegram', 'Telegram')],
                                      ondelete={"telegram": "cascade"})