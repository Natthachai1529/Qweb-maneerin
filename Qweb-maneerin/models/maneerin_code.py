from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")  
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller = fields.Many2one(comodel_name="res.partner", string="ผู้จะขาย")  # ผู้ขายเป็น res.partner
    
    # เปลี่ยนเป็น Many2many เพื่อเชื่อมโยงกับ res.partner
    buyer_ids = fields.Many2many(comodel_name='res.partner', string="ผู้จะซื้อ")  
    beneficiary_ids = fields.Many2many(comodel_name='res.partner', string="ผู้รับสิทธิ์") 

