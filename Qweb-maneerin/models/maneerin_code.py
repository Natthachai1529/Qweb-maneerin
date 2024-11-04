from odoo import models, fields, api

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
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้ซื้อ")  # เปลี่ยนเป็น Many2one เพื่อเลือกจาก res.partner
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.age = self.partner_id.age  # ปรับให้ดึงข้อมูลอายุจาก res.partner
            self.nation = self.partner_id.nationality  # ปรับให้ดึงข้อมูลสัญชาติ
            self.street = self.partner_id.street  # ปรับให้ดึงข้อมูลถนน
            self.phone = self.partner_id.phone  # ปรับให้ดึงข้อมูลโทรศัพท์

class ManeerinCodeBeneficiary(models.Model):
    _name = 'maneerincode.beneficiary'
    
    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้รับสิทธิ์")  # เปลี่ยนเป็น Many2one เพื่อเลือกจาก res.partner
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.age = self.partner_id.age  # ปรับให้ดึงข้อมูลอายุจาก res.partner
            self.nation = self.partner_id.nationality  # ปรับให้ดึงข้อมูลสัญชาติ
            self.street = self.partner_id.street  # ปรับให้ดึงข้อมูลถนน
            self.phone = self.partner_id.phone  # ปรับให้ดึงข้อมูลโทรศัพท์
