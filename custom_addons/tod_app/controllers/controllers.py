# -*- coding: utf-8 -*-
# from odoo import http


# class TodApp(http.Controller):
#     @http.route('/tod_app/tod_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tod_app/tod_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tod_app.listing', {
#             'root': '/tod_app/tod_app',
#             'objects': http.request.env['tod_app.tod_app'].search([]),
#         })

#     @http.route('/tod_app/tod_app/objects/<model("tod_app.tod_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tod_app.object', {
#             'object': obj
#         })
