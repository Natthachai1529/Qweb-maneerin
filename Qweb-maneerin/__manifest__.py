{
    'name': 'Qweb',
    'summary': 'Module For Qweb maneerin',
    'description': 'This module manages Qweb reports for Maneerin Codes.',
    'depends': ['base', 'contacts'],  
    'data': [
        'security/ir.model.access.csv',
        'button/ButtonTag.xml',
        'views/views.xml',
        'views/view_addon_contact.xml',
        'view/Report_Maneerin_Template.xml',
    ],
    'application': True,
    'installable': True,
}
