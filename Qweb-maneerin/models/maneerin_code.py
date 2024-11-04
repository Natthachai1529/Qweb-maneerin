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
    age = fields.Integer(string="Age", readonly=True)
    nation = fields.Char(string="Nation", readonly=True)
    street = fields.Char(string="Street", readonly=True)
    phone = fields.Char(string="Phone", readonly=True)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.age = self.partner_id.age  # ดึงอายุจาก res.partner
            self.nation = self.partner_id.nationality  # ดึงสัญชาติจาก res.partner
            self.street = self.partner_id.street  # ดึงถนนจาก res.partner
            self.phone = self.partner_id.phone  # ดึงเบอร์โทรจาก res.partner

class ManeerinCodeBeneficiary(models.Model):
    _name = 'maneerincode.beneficiary'
    
    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้รับสิทธิ์")  # เปลี่ยนเป็น Many2one เพื่อเลือกจาก res.partner
    age = fields.Integer(string="Age", readonly=True)
    nation = fields.Char(string="Nation", readonly=True)
    street = fields.Char(string="Street", readonly=True)
    phone = fields.Char(string="Phone", readonly=True)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.age = self.partner_id.age  # ดึงอายุจาก res.partner
            self.nation = self.partner_id.nationality  # ดึงสัญชาติจาก res.partner
            self.street = self.partner_id.street  # ดึงถนนจาก res.partner
            self.phone = self.partner_id.phone  # ดึงเบอร์โทรจาก res.partner
