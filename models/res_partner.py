from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(string='Age')
    nation = fields.Char(string='Nation')
    thai_id = fields.Char(string='เลขประจำตัวประชาชน')
   
     # Override the title field to add Thai titles
    title = fields.Many2one(
        'res.partner.title',
        string='คำนำหน้าชื่อ',
    )
    
    @api.onchange('company_type')
    def _onchange_company_type(self):
        # Clear title when changing to company type
        if self.company_type == 'company':
            self.title = False