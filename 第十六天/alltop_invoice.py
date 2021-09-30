from odoo import models, fields, api
from odoo.tools import datetime


class alltop_invoice(models.Model):
    _name = 'alltop_freezer.alltop_invoice'
    _description = '開票'

    tax = fields.Integer(string='營業稅小計', compute='compute_amount')
    amount_total = fields.Integer(string='合計', compute='compute_amount', store=True)
    # invoce_line_ids = fields.One2many('alltop.invoice.line', 'invoice_id')
    # lessess = fields.Char(string='承銷號', related='partner_id.lessee')
    date = fields.Date(string='制表日期', default=datetime.today().strftime('%Y-%m-%d'))
    organizer = fields.Many2one(comodel_name='res.users', string='製表人員')
    # monthly_id = fields.Many2one('alltop.freezer.monthly')

