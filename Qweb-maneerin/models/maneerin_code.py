from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")  
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller = fields.Many2one(comodel_name="res.partner", string="ผู้จะขาย")

    buyer_ids = fields.One2many(comodel_name='maneerincode.buyer', inverse_name='maneerincode_id', string="ผู้จะซื้อ")  
    beneficiary_ids = fields.One2many(comodel_name='maneerincode.beneficiary', inverse_name='maneerincode_id', string="ผู้รับสิทธิ์") 

    def action_print_report(self):
        # ฟังก์ชันปริ้นรายงาน
        return {
            'type': 'ir.actions.report',
            'report_name': 'your_module_name.report_template_name',  # ใส่ชื่อของ template ที่จะใช้
            'report_type': 'qweb-pdf',
            'model': 'maneerincode.code',
            'res_id': self.id,
        }

class ManeerinCodeBuyer(models.Model):
    _name = 'maneerincode.buyer'
    
    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้ซื้อ")  
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone", related='partner_id.phone', store=True)

class ManeerinCodeBeneficiary(models.Model):
    _name = 'maneerincode.beneficiary'
    
    maneerincode_id = fields.Many2one(comodel_name='maneerincode.code', string="Maneerin Code")
    partner_id = fields.Many2one(comodel_name='res.partner', string="ผู้รับสิทธิ์")  
    age = fields.Integer(string="Age")
    nation = fields.Char(string="Nation")
    street = fields.Char(string="Street")
    phone = fields.Char(string="Phone", related='partner_id.phone', store=True)
