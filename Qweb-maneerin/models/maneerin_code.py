from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller_id = fields.Many2one('res.partner', string="ผู้จะขาย")  # เชื่อมโยงกับโมเดล res.partner
    buyer_ids = fields.One2many('buyer.info', 'maneerin_code_id', string="ผู้จะซื้อ")
    beneficiary_ids = fields.One2many('beneficiary.info', 'maneerin_code_id', string="ผู้รับสิทธิ์โอน")

class BuyerInfo(models.Model):
    _name = 'buyer.info'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone")
    maneerin_code_id = fields.Many2one('maneerincode.code', string="Maneerin Code")
    buyer_id = fields.Many2one('res.partner', string="ผู้ซื้อ")  # เชื่อมโยงกับโมเดล res.partner

class BeneficiaryInfo(models.Model):
    _name = 'beneficiary.info'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone")
    maneerin_code_id = fields.Many2one('maneerincode.code', string="Maneerin Code")
