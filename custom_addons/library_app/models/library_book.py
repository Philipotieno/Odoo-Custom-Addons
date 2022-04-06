# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active", default=True)
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner", string="Publisher")
    authors_id = fields.Many2many("res.partner", string="Authors")
