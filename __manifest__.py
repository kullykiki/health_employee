# -*- coding: utf-8 -*-
{
    'name': "health_employee",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kully",
    'website': "http://www.kully.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': ['base','hr','web'],
    'assets': {
        'web.assets_backend': [
            'health_employee/static/src/**/*'
        ]
    },
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
}