{
    'name': 'Qweb',
    'summary': 'Module For Qweb maneerin',
    'description': 'This module manages Qweb reports for Maneerin Codes.',
    'depends': ['base', 'contacts'],  
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/maneerin_contract.xml',  
    ],

    'application': True,
    'installable': True,
}
