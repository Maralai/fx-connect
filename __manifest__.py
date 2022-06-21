# -*- coding: utf-8 -*-
{
    'name': "FX-Connect",

    'summary': """
        This application is designed to interface with FX CONNECT from Zebra.""",

    'description': """
    """,

    'author': "Harrison Consulting, LLC",
    'website': "http://harrison.consulting",
    'license':'GPL-3',
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/access_rights.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
