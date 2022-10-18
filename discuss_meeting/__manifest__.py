# -*- coding: utf-8 -*-


{
    'name': 'Meeting',
    'category': 'Productivity/Discuss',
    'summary': 'Meeting',
    'description': "Meeting",
    'depends': ['base', 'mail', 'discuss'],
    'application': True,
    'assets': {
        'web.assets_qweb': [
            'discuss_meeting/static/src/components/discuss_meeting/meeting_views.xml',
        ],
    },
    'license': 'LGPL-3',
}
