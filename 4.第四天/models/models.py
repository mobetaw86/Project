# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api
from odoo.tools import datetime


class alltop_freezer(models.Model):
    _name = 'alltop_freezer.alltop_freezer'
    _description = '庫房'

    name = fields.Char(string='庫號')
    square_feet = fields.Float(string='坪數')
    price_unit = fields.Integer(string='每坪租金')
    price_total = fields.Integer(string='租金總額', compute='_compute_price_total', store=True)
    partner_id = fields.Many2one('res.partner', string='使用人')
    date_start = fields.Date(string='承租日期-起', default=datetime.today().strftime('%Y-%m-%d'))
    date_end = fields.Date(string='承租日期-迄', default=datetime.today() + relativedelta(months=1))

    @api.depends('square_feet', 'price_unit')
    def _compute_price_total(self):
        for record in self:
            record.price_total = record.square_feet * record.price_uni