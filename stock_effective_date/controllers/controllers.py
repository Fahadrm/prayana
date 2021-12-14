# -*- coding: utf-8 -*-
# from odoo import http


# class StockEffectiveDate(http.Controller):
#     @http.route('/stock_effective_date/stock_effective_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_effective_date/stock_effective_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_effective_date.listing', {
#             'root': '/stock_effective_date/stock_effective_date',
#             'objects': http.request.env['stock_effective_date.stock_effective_date'].search([]),
#         })

#     @http.route('/stock_effective_date/stock_effective_date/objects/<model("stock_effective_date.stock_effective_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_effective_date.object', {
#             'object': obj
#         })
