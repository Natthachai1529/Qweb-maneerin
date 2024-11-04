from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")  
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller = fields.Char(string="ผู้จะขาย")
    buyer = fields.Char(string="ผู้จะซื้อ")  
    beneficiary = fields.Char(string="ผู้รับสิทธิ์")
