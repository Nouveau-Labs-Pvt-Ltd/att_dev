# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ATTProduct(models.Model):
    _inherit = ['product.template']

    customer_id = fields.Many2one('res.partner', string='Customer', 
                                  help="You can find a customer by its Name, TIN, Email or Internal Reference.")