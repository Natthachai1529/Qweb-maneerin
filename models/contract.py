from odoo import api, fields, models
from datetime import datetime

class Contract(models.Model):
    _name = 'contract.contract'
    _description = 'Contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # เพิ่มการ inherit mail.thread เพื่อใช้ tracking

    name = fields.Char(string='Contract Number', required=True,
                      default=lambda self: self.env['ir.sequence'].next_by_code('contract.sequence'))
    contract_date = fields.Date(string='Contract Date', default=fields.Date.context_today)
    seller_id = fields.Many2one('res.partner', string='ผู้จะขาย', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', tracking=True)  # tracking จะทำงานเมื่อ inherit mail.thread
    
    buyer_ids = fields.One2many('contract.buyer.line', 'contract_id', string='ผู้จะซื้อ')
    transferee_ids = fields.One2many('contract.transferee.line', 'contract_id', string='ผู้รับโอนสิทธิ์')
    project_name = fields.Char(string='โครงการ', required=True)
    land_id = fields.Char(string='แปลงที่', required=True)

    def get_thai_date(self, date):
        if not date:
            return ""    
        THAI_MONTHS = {
            '1': 'มกราคม',
            '2': 'กุมภาพันธ์',
            '3': 'มีนาคม',
            '4': 'เมษายน',
            '5': 'พฤษภาคม',
            '6': 'มิถุนายน',
            '7': 'กรกฎาคม',
            '8': 'สิงหาคม',
            '9': 'กันยายน',
            '10': 'ตุลาคม',
            '11': 'พฤศจิกายน',
            '12': 'ธันวาคม'
        }

        date_obj = datetime.strptime(str(date), '%Y-%m-%d')
        thai_year = date_obj.year + 543
        thai_month = THAI_MONTHS[str(date_obj.month)]
        return f"{date_obj.day} {thai_month} {thai_year}"

class ContractBuyerLine(models.Model):
    _name = 'contract.buyer.line'
    _description = 'Contract Buyer Line'

    active = fields.Boolean(default=True)
    contract_id = fields.Many2one('contract.contract', string='Contract')
    partner_id = fields.Many2one('res.partner', string='Name', required=True)
    title = fields.Many2one(related='partner_id.title', string='คำนำหน้าชื่อ', readonly=True)
    age = fields.Integer(related='partner_id.age', string='Age', readonly=True)
    nation = fields.Char(related='partner_id.nation', string='Nation', readonly=True)
    street = fields.Char(related='partner_id.street', string='Street', readonly=True)
    phone = fields.Char(related='partner_id.phone', string='Phone', readonly=True)

    def unlink(self):
        # Instead of deleting, archive the record
        self.write({'active': False})
        return True

class ContractTransfereeLine(models.Model):
    _name = 'contract.transferee.line'
    _description = 'Contract Transferee Line'

    active = fields.Boolean(default=True)
    contract_id = fields.Many2one('contract.contract', string='Contract')
    partner_id = fields.Many2one('res.partner', string='Name', required=True)
    title = fields.Many2one(related='partner_id.title', string='คำนำหน้าชื่อ', readonly=True)
    age = fields.Integer(related='partner_id.age', string='Age', readonly=True)
    nation = fields.Char(related='partner_id.nation', string='Nation', readonly=True)
    street = fields.Char(related='partner_id.street', string='Street', readonly=True)
    phone = fields.Char(related='partner_id.phone', string='Phone', readonly=True)

    def unlink(self):
        # Instead of deleting, archive the record
        self.write({'active': False})
        return True