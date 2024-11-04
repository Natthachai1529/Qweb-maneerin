from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contact_date = fields.Date(string='Contact Date', default=fields.Date.now)  
    seller = fields.Char(string="ผู้จะขาย")
    buyer = fields.Char(string="ผู้จะซื้อ")  
    beneficiary = fields.Char(string="ผู้รับสิทธิ์")
