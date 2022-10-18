# -*- coding: utf-8 -*-


{
    'name': 'Discuss',
    'category': 'Productivity/Discuss',
    'summary': 'Discuss',
    'description': "Discuss",
    'depends': ['base', 'mail'],
    'data': [
        'views/contact_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'views/discuss_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'discuss/static/src/components/*/*.js',
            'discuss/static/src/components/*/*.scss',
            'discuss/static/src/widgets/*/*.js',
            'discuss/static/src/widgets/*/*.scss',
            'discuss/static/src/js/**/*.js',
        ],
        'web.assets_qweb': [
            'discuss/static/src/xml/*.xml',
            'discuss/static/src/components/*/*.xml',
            'discuss/static/src/widgets/*/*.xml',
        ],
        'web.assets_backend_prod_only': [
            'discuss/static/src/main.js',
        ],
    }
}
