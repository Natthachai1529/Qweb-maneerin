from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contact_date = fields.Date(string='Contact Date')
    seller = fields.Char(string="ผู้ขาย")
