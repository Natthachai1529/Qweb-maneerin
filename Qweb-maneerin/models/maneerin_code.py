from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller = fields.Char(string="ผู้จะขาย")
    buyer_ids = fields.One2many('buyer.code', 'maneerincode_id', string="ผู้จะซื้อ")
    beneficiary_ids = fields.One2many('beneficiary.code', 'maneerincode_id', string="ผู้รับสิทธิ์")

class BuyerCode(models.Model):
    _name = 'buyer.code'

    name = fields.Char(string="ชื่อผู้ซื้อ")
    maneerincode_id = fields.Many2one('maneerincode.code', string="สัญญา")

class BeneficiaryCode(models.Model):
    _name = 'beneficiary.code'

    name = fields.Char(string="ชื่อผู้รับสิทธิ์")
    maneerincode_id = fields.Many2one('maneerincode.code', string="สัญญา")
