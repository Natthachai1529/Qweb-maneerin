{
    'name': 'Qweb',
    'summary': 'Module For Qweb maneerin',
    'description': 'This module manages Qweb reports for Maneerin Codes.',
    'depends': ['base', 'contacts'],  
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml', 
    ],
    'application': True,
    'installable': True,
}
