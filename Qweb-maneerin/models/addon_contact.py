from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    age2 = fields.Integer(string='Age')
    nation2 = fields.Char(string='Nationality')
    identification_number = fields.Char(string='Identification Number')
