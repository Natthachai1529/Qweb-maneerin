from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")  
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller = fields.Many2one(comodel_name="res.partner", string="ผู้จะขาย")

    buyer_ids = fields.One2many(comodel_name='maneerincode.buyer', inverse_name='maneerincode_id', string="ผู้จะซื้อ")  
    beneficiary_ids = fields.One2many(comodel_name='maneerincode.beneficiary', inverse_name='maneerincode_id', string="ผู้รับสิทธิ์") 

class ManeerinCodeBuyer(models.Model):
    _name = 'maneerincode.buyer'
    
    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้ซื้อ")  # เลือกจาก res.partner
    
    # ฟิลด์ที่ใช้ related
    age = fields.Integer(related='partner_id.age', string='Age', readonly=True)
    nation = fields.Char(related='partner_id.nationality', string='Nation', readonly=True)  # ใช้ 'nationality' แทน 'nation'
    street = fields.Char(related='partner_id.street', string='Street', readonly=True)
    phone = fields.Char(related='partner_id.phone', string='Phone', readonly=True)

class ManeerinCodeBeneficiary(models.Model):
    _name = 'maneerincode.beneficiary'
    
    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้รับสิทธิ์")  # เลือกจาก res.partner
    
    # ฟิลด์ที่ใช้ related
    age = fields.Integer(related='partner_id.age', string='Age', readonly=True)
    nation = fields.Char(related='partner_id.nationality', string='Nation', readonly=True)  # ใช้ 'nationality' แทน 'nation'
    street = fields.Char(related='partner_id.street', string='Street', readonly=True)
    phone = fields.Char(related='partner_id.phone', string='Phone', readonly=True)
