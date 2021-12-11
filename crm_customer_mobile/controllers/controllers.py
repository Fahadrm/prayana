# -*- coding: utf-8 -*-
# from odoo import http


# class CrmCustomerMobile(http.Controller):
#     @http.route('/crm_customer_mobile/crm_customer_mobile/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_customer_mobile/crm_customer_mobile/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_customer_mobile.listing', {
#             'root': '/crm_customer_mobile/crm_customer_mobile',
#             'objects': http.request.env['crm_customer_mobile.crm_customer_mobile'].search([]),
#         })

#     @http.route('/crm_customer_mobile/crm_customer_mobile/objects/<model("crm_customer_mobile.crm_customer_mobile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_customer_mobile.object', {
#             'object': obj
#         })
