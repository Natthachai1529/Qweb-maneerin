from odoo import models, fields

class maneerincode(models.Model):
    _name = 'maneerincode.code'

    vendor = fields.Many2one(comodel_name='res.partner', string='Vendor')
    v_ref = fields.Char(string='Vendor Reference') 
    order_deadline = fields.Datetime(string="Order Deadline")
    expected_arrival = fields.Datetime(string="Expected Arrival")
    
