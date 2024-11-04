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
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้ซื้อ")
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.age = self.partner_id.age or 0  # หรือใช้ค่า default อื่นๆ
            self.nation = self.partner_id.country_id.name if self.partner_id.country_id else ''
            self.street = self.partner_id.street or ''
            self.phone = self.partner_id.phone or ''

class ManeerinCodeBeneficiary(models.Model):
    _name = 'maneerincode.beneficiary'
    
    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้รับสิทธิ์")
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.age = self.partner_id.age or 0  # หรือใช้ค่า default อื่นๆ
            self.nation = self.partner_id.country_id.name if self.partner_id.country_id else ''
            self.street = self.partner_id.street or ''
            self.phone = self.partner_id.phone or ''
