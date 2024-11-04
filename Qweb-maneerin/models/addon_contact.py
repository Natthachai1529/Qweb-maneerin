from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(string='Age')
    nation = fields.Char(string='Nation')
    thai_id = fields.Char(string='Identification Number')
