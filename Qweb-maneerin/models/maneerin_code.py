from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")  
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller = fields.Char(string="ผู้จะขาย")
    buyer_id = fields.Many2one('maneerincode.buyer', string="ผู้จะซื้อ")
    beneficiary_id = fields.Many2one('maneerincode.beneficiary', string="ผู้รับสิทธิ์")

class Buyer(models.Model):
    _name = 'maneerincode.buyer'

    name = fields.Char(string="ชื่อ")
    age = fields.Integer(string="อายุ")
    nation = fields.Char(string="สัญชาติ")
    street = fields.Char(string="ถนน")
    phone = fields.Char(string="โทรศัพท์")

class Beneficiary(models.Model):
    _name = 'maneerincode.beneficiary'

    name = fields.Char(string="ชื่อ")
    age = fields.Integer(string="อายุ")
    nation = fields.Char(string="สัญชาติ")
    street = fields.Char(string="ถนน")
    phone = fields.Char(string="โทรศัพท์")
