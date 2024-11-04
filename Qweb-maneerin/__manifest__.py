{
    'name': 'Qweb',
    'summary': 'Module For Qweb maneerin',
    'description': 'This module manages Qweb reports for Maneerin Codes.',
    'depends': ['base', 'contact'],  
    'data': [
        'security/ir.model.access.csv',
        'button/ButtonTag.xml',
        'views/views.xml',
        'views/view_addon_contact.xml', 
    ],
    'application': True,
    'installable': True,
}
