from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")  
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller_id = fields.Many2one(comodel_name="res.partner", string="ผู้จะขาย")  # เปลี่ยนเป็น seller_id

    buyer_ids = fields.One2many('maneerincode.buyer', 'maneerincode_id', string="ผู้จะซื้อ")  
    beneficiary_ids = fields.One2many('maneerincode.beneficiary', 'maneerincode_id', string="ผู้รับสิทธิ์") 

class ManeerinCodeBuyer(models.Model):
    _name = 'maneerincode.buyer'
    
    maneerincode_id = fields.Many2one('maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one('res.partner', string="ผู้ซื้อ")  # เชื่อมโยงกับ res.partner

    # ฟิลด์เพื่อดึงข้อมูลจาก partner_id
    name = fields.Char(related='partner_id.name', string="Name", store=True)
    age = fields.Integer(related='partner_id.age', string="Age", store=True)
    nation = fields.Char(related='partner_id.nation', string="Nation", store=True)
    street = fields.Char(related='partner_id.street', string="Street", store=True)
    phone = fields.Char(related='partner_id.phone', string="Phone", store=True)

class ManeerinCodeBeneficiary(models.Model):
    _name = 'maneerincode.beneficiary'
    
    maneerincode_id = fields.Many2one('maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one('res.partner', string="ผู้รับสิทธิ์")  # เชื่อมโยงกับ res.partner

    # ฟิลด์เพื่อดึงข้อมูลจาก partner_id
    name = fields.Char(related='partner_id.name', string="Name", store=True)
    age = fields.Integer(related='partner_id.age', string="Age", store=True)
    nation = fields.Char(related='partner_id.nation', string="Nation", store=True)
    street = fields.Char(related='partner_id.street', string="Street", store=True)
    phone = fields.Char(related='partner_id.phone', string="Phone", store=True)
