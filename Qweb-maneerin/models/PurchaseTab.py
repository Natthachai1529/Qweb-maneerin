from odoo import models, fields

class PurchaseTab(models.Model):
    _name = 'purchase.tab.code'

    purchase_management_id = fields.Many2one(
        comodel_name='purchase.management.code', 
        string='Purchase Management'
    )
    product_id = fields.Many2one(
        comodel_name='product.template',  
        string='Product'
    )

    description = fields.Char(string='Description') 
    expected_arrival2 = fields.Datetime(string='Expected Arrival') 
    quantity = fields.Float(string='Quantity')  
    unit_price = fields.Float(string='Unit Price')  
    taxes = fields.Float(string='Taxes')  
    disc = fields.Float(string='Discount%')  
    tax_excl = fields.Float(string='Tax Excluding')  
    tax_incl = fields.Float(string='Tax Including')  