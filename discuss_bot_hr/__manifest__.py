# -*- coding: utf-8 -*-
{
    'name': "discuss_bot_hr",
    'summary': """Bridge module between hr and mailbot.""",
    'description': """This module adds the Discuss Bot state and notifications in the user form modified by hr.""",
    'category': 'Productivity/Discuss',
    'version': '1.0',
    'depends': ['discuss_bot', 'hr'],
    'application': False,
    'installable': True,
    'auto_install': True,
    'data': [
        'views/res_users_views.xml',
    ],
    'license': 'LGPL-3',
}
