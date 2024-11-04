from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contact_date = fields.Datetime(string='Contact Date', default=fields.Datetime.now)  # เปลี่ยนเป็น fields.Datetime.now
    seller = fields.Char(string="ผู้จะขาย")
    buyer = fields.Char(string="ผู้จะซื้อ")  
    beneficiary = fields.Char(string="ผู้รับสิทธิ์")
