{
    'name': 'Qweb',
    'summary': 'Module For Qweb maneerin',
    'depends': ['base', 'contacts', 'web', 'report'],  
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',  
        'reports/report_maneerincode.xml',
    ],
    'application': True,
}
