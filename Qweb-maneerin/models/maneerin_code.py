from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")  
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller = fields.Many2one(comodel_name="res.partner", string="ผู้จะขาย")  # ผู้ขายเป็น res.partner

    # ใช้ One2many เพื่อเชื่อมโยงไปยังโมเดลที่สร้างขึ้น
    buyer_ids = fields.One2many('maneerincode.buyer', 'maneerincode_id', string="ผู้จะซื้อ")  
    beneficiary_ids = fields.One2many('maneerincode.beneficiary', 'maneerincode_id', string="ผู้รับสิทธิ์") 

class ManeerinCodeBuyer(models.Model):
    _name = 'maneerincode.buyer'
    
    maneerincode_id = fields.Many2one('maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one('res.partner', string="ผู้ซื้อ")  # ฟิลด์เพื่อเชื่อมโยงกับ res.partner
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone")

class ManeerinCodeBeneficiary(models.Model):
    _name = 'maneerincode.beneficiary'
    
    maneerincode_id = fields.Many2one('maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one('res.partner', string="ผู้รับสิทธิ์")  # ฟิลด์เพื่อเชื่อมโยงกับ res.partner
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone")
