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
        'reports/button_tag.xml',
        'reports/connect_report.xml',
        'reports/format_report.xml',
        'reports/report_maneerin_template.xml',
    ],
    'application': True,
    'installable': True,
}
