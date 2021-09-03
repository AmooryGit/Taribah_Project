# -*- coding: utf-8 -*-
# from odoo import http


# class TaribahProject(http.Controller):
#     @http.route('/taribah_project/taribah_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/taribah_project/taribah_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('taribah_project.listing', {
#             'root': '/taribah_project/taribah_project',
#             'objects': http.request.env['taribah_project.taribah_project'].search([]),
#         })

#     @http.route('/taribah_project/taribah_project/objects/<model("taribah_project.taribah_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('taribah_project.object', {
#             'object': obj
#         })
