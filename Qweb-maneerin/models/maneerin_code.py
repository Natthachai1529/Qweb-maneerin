from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char(string="เลขที่สัญญา")
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today)
    seller_id = fields.Many2one('res.partner', string="ผู้จะขาย")  # เพิ่มฟิลด์นี้
    buyer_ids = fields.One2many('buyer.model', 'maneerin_code_id', string="ผู้จะซื้อ")  # ให้แน่ใจว่าฟิลด์นี้ถูกสร้างแล้ว
    beneficiary_ids = fields.One2many('beneficiary.model', 'maneerin_code_id', string="ผู้รับสิทธิ์")  # ให้แน่ใจว่าฟิลด์นี้ถูกสร้างแล้ว
