# -*- coding: utf-8 -*-
{
    'name': "Configurations",
    'summary': """Config""",
    'description': """Config """,
    'author': "Black Belts Egypt",
    'website': "www.blackbelts-egypt.com",
    'category': 'arope-conf',
    'version': '0.1',
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base','helpdesk_inherit'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'security/security.xml',
        'views/policy_view.xml',
        'views/collection.xml',
        'views/claim.xml',
        # 'views/setup.xml',
        # 'views/covers.xml',
        # 'views/motor_setup.xml',
        'views/main_setup.xml',
        # 'views/travel_priceTable.xml',
        'views/partner.xml',

        # 'views/travel_rating_table.xml',
        'views/menu.xml',
        'wizard/users.xml',
        'wizard/curr_wiz.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
