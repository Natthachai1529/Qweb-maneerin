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
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้ซื้อ")

    name = fields.Char(string="Name", related='partner_id.name', store=True)
    age = fields.Integer(string="Age", related='partner_id.age', store=True)
    nation = fields.Char(string="Nation", related='partner_id.nation', store=True)
    street = fields.Char(string="Street", related='partner_id.street', store=True)
    phone = fields.Char(string="Phone", related='partner_id.phone', store=True)

class ManeerinCodeBeneficiary(models.Model):
    _name = 'maneerincode.beneficiary'

    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้รับสิทธิ์")

    name = fields.Char(string="Name", related='partner_id.name', store=True)
    age = fields.Integer(string="Age", related='partner_id.age', store=True)
    nation = fields.Char(string="Nation", related='partner_id.nation', store=True)
    street = fields.Char(string="Street", related='partner_id.street', store=True)
    phone = fields.Char(string="Phone", related='partner_id.phone', store=True)
