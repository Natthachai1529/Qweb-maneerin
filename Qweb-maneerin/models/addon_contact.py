from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(string='Age')
    nation = fields.Char(string='Nationality')
    identification_number = fields.Char(string='Identification Number')
