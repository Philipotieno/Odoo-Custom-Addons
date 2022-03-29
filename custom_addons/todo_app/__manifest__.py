# -*- coding: utf-8 -*-
{
    'name': "To-Do Application",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Manage personal to tasks
    """,

    'author': "Philip Otieno",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "sequence": -103,
    'category': 'Productivity',

    'version': "15.0.1.0.0",
    'depends': ['base'],
    'data': [
        'views/todo_menu.xml',
        'views/todo_view.xml'
    ],
    "installable": True,
    "application": True,
}
