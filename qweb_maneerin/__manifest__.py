{
    'name': 'Qweb',
    'summary': 'Module For Qweb maneerin',
    'description': 'This module manages Qweb reports for Maneerin Codes.',
    'version': '17.0.1.0.0',
    'depends': ['base', 'contacts'],  
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/view_addon_contact.xml',
        
        'reports/connect_report.xml',
        'reports/format_report.xml',
        'reports/report_maneerin_template.xml',
    ],
    'application': True,
    'installable': True,
}
