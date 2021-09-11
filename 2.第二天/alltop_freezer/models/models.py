# -*- coding: utf-8 -*-

from odoo import models, fields, api


class alltop_freezer(models.Model):
    _name = 'alltop_freezer.alltop_freezer'
    _description = 'alltop_freezer.alltop_freezer'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
