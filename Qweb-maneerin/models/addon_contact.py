from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_age = fields.Integer(string='Age')
    partner_nation = fields.Char(string='Nationality')
    identification_number = fields.Char(string='Identification Number')
