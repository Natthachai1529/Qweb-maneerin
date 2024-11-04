{
    'name': 'Qweb',
    'summary': 'Module For Qweb maneerin',
    'description': 'This module manages Qweb reports for Maneerin Codes.',
    'depends': ['base', 'contacts'],  
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/maneerin_contract.xml',
        'views/views.xml',
        'reports/report_maneerin_contract.xml',  
    ],
    'application': True,
    'installable': True,
}
