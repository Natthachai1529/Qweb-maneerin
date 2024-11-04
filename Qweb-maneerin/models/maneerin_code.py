from odoo import models, fields, api

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today)
    seller = fields.Many2one(comodel_name="res.partner", string="ผู้จะขาย")
    
    buyer_ids = fields.One2many(comodel_name='maneerincode.buyer', inverse_name='maneerincode_id', string="ผู้จะซื้อ")  
    beneficiary_ids = fields.One2many(comodel_name='maneerincode.beneficiary', inverse_name='maneerincode_id', string="ผู้รับสิทธิ์")

    def action_print_report(self):
        return self.env.ref('maneerin.report_maneerincode').report_action(self)

class ManeerinCodeBuyer(models.Model):
    _name = 'maneerincode.buyer'
    
    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    name = fields.Many2one(comodel_name='res.partner', string="Name")
    age = fields.Integer(string="Age", related='name.age', store=True)
    nation = fields.Char(string="Nation", related='name.nationality', store=True)
    street = fields.Char(string="Street", related='name.street', store=True)
    phone = fields.Char(string="Phone", related='name.phone', store=True)

class ManeerinCodeBeneficiary(models.Model):
    _name = 'maneerincode.beneficiary'
    
    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    name = fields.Many2one(comodel_name='res.partner', string="Name")
    age = fields.Integer(string="Age", related='name.age', store=True)
    nation = fields.Char(string="Nation", related='name.nationality', store=True)
    street = fields.Char(string="Street", related='name.street', store=True)
    phone = fields.Char(string="Phone", related='name.phone', store=True)
