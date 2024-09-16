# -*- coding: utf-8 -*-

from odoo import models, fields, api

class health_employee(models.Model):
    _name = 'health_employee.health_employee'
    _description = 'Record Health Employee'

    name = fields.Char()
    description = fields.Text()
    employee = fields.Many2one('hr.employee','Employee')

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    health_employee = fields.Char()