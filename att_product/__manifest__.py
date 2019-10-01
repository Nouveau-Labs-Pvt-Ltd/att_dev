# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AT&T Product',
    'version': '1.0',
    'category': 'Sales',
    'description': """
Set Customer on Product
=======================

Add customer and product one to one relationship:
-------------------------------------------------
    * Customer
    
    """,
    'depends': ['sale'],
    'data': [
        #'security/ir.model.access.csv',
        'views/att_product_views.xml',
    ],
    'installable': True,
}
