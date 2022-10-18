# -*- coding: utf-8 -*-


{
    'name': 'Discuss Bot',
    'version': '1.2',
    'category': 'Productivity/Discuss',
    'summary': 'Add Discuss Bot in discussions',
    'description': "",
    'depends': ['mail'],
    'auto_install': True,
    'installable': True,
    'application': False,
    'data': [
        'views/res_users_views.xml',
        'data/discussbot_data.xml',
    ],
    'demo': [
        'data/discussbot_demo.xml',
    ],
    'assets': {
        'mail.assets_discuss_public': [
            'discuss_bot/static/src/models/*/*.js',
        ],
        'web.assets_backend': [
            'discuss_bot/static/src/models/*/*.js',
            'discuss_bot/static/src/scss/discussbot_style.scss',
        ],
        'web.tests_assets': [
            'discuss_bot/static/tests/**/*',
        ],
        'web.qunit_suite_tests': [
            'discuss_bot/static/src/models/*/tests/*.js',
        ],
    },
    'license': 'LGPL-3',
}
