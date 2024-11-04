from odoo import models, fields

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contract_no = fields.Char 
    contact_date = fields.Date(string='Contact Date', default=fields.Date.today) 
    seller = fields.Char(string="ผู้จะขาย")
    buyer_id = fields.Many2one('res.partner', string="ผู้จะซื้อ")  
    beneficiary_id = fields.Many2one('res.partner', string="ผู้รับสิทธิ์")
