from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type_messenger = fields.Selection(string='Type Messenger',
                                      selection=[('none', 'None')],
                                      default='none')