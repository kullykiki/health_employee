# -*- coding: utf-8 -*-
from odoo import http

# class HealthEmployee(http.Controller):
#     @http.route('/health_employee/health_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/health_employee/health_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('health_employee.listing', {
#             'root': '/health_employee/health_employee',
#             'objects': http.request.env['health_employee.health_employee'].search([]),
#         })

#     @http.route('/health_employee/health_employee/objects/<model("health_employee.health_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('health_employee.object', {
#             'object': obj
#         })