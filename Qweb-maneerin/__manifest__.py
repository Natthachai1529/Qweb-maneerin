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
        'reports/Connect_Report.xml',
        'reports/Format_Report.xml',
        'reports/Report_Maneerin_Template.xml',
    ],
    'application': True,
    'installable': True,
}
