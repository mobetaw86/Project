# -*- coding: utf-8 -*-

from odoo import http


class AlltopFreezer(http.Controller):
    @http.route('/alltop_freezer/alltop_freezer/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/alltop_freezer/alltop_freezer/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('alltop_freezer.listing', {
            'root': '/alltop_freezer/alltop_freezer',
            'objects': http.request.env['alltop_freezer.alltop_freezer'].search([]),
        })

    @http.route('/alltop_freezer/alltop_freezer/objects/<model("alltop_freezer.alltop_freezer"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('alltop_freezer.object', {
            'object': obj
        })
