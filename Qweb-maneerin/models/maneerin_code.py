from odoo import models, fields
from datetime import datetime

class ManeerinCode(models.Model):
    _name = 'maneerincode.code'

    contact_date = fields.Datetime(string='Contact Date', default=datetime.now)
    seller = fields.Char(string="ผู้จะขาย")
    buyer = fields.Char(string="ผู้จะซื้อ")
    beneficiary = fields.Char(string="ผู้รับสิทธิ์")
