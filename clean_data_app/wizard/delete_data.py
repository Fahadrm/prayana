# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class DeleteData(models.TransientModel):
    _name = "delete.data"
    _description = "Delete Data Record"

    sale_transfer = fields.Boolean("Sales & All Transfers")
    purchase_transfer = fields.Boolean("Purchase & All Transfers")
    only_transfers = fields.Boolean("Only Transfers")
    invoicing_payments_journal_entries = fields.Boolean('All Invoicing, Payments & Journal Entries')
    only_journal_entries = fields.Boolean("Only Journal Entries")
    customers_vendors = fields.Boolean("Customers & Vendors")
    accounts_ccounting = fields.Boolean("Chart Of Accounts & All Accounting Data")
    all_data = fields.Boolean("All Data")


    @api.onchange('all_data')
    def onchange_all_data(self):
        if self.all_data:
            self.sale_transfer = True
            self.purchase_transfer = True
            self.only_transfers = True
            self.invoicing_payments_journal_entries = True
            self.only_journal_entries = True
            self.customers_vendors = True
            self.accounts_ccounting = True
        if not self.all_data:
            self.sale_transfer = False
            self.purchase_transfer = False
            self.only_transfers = False
            self.invoicing_payments_journal_entries = False
            self.only_journal_entries = False
            self.customers_vendors = False
            self.accounts_ccounting = False


    def save_data(self):
        if self.sale_transfer:
            order_id = self.env.cr.execute("""SELECT id FROM sale_order""")
            sale_order_ids = self.env.cr.fetchall()
            order_ids = []
            for sale_order_id in sale_order_ids:
                order_ids.append(sale_order_id[0])
            if order_ids:
                picking_query_exe = self.env.cr.execute("SELECT id FROM stock_picking WHERE sale_id in %s", (tuple(order_ids),))
                picking_ids_fetchall = self.env.cr.fetchall()
                picking_ids = []
                for picking_id in picking_ids_fetchall:
                    picking_ids.append(picking_id[0])
                if picking_ids:
                    move_query_exe = self.env.cr.execute("SELECT id FROM stock_move WHERE picking_id in %s", (tuple(picking_ids),))
                    move_ids_fetchall = self.env.cr.fetchall()
                    move_ids = []
                    for move_id in move_ids_fetchall:
                        move_ids.append(move_id[0])
                    if move_ids:
                        move_line_query_exe = self.env.cr.execute("SELECT id FROM stock_move_line WHERE move_id in %s", (tuple(move_ids),))
                        move_line_ids_fetchall = self.env.cr.fetchall()
                        move_line_ids = []
                        for move_line_id in move_line_ids_fetchall:
                            move_line_ids.append(move_line_id[0])
                        if move_line_ids:
                            self.env.cr.execute("DELETE FROM stock_move_line WHERE id in %s", (tuple(move_line_ids),))
                        self.env.cr.execute("DELETE FROM stock_move WHERE id in %s", (tuple(move_ids),))
                    self.env.cr.execute("DELETE FROM stock_picking WHERE id in %s", (tuple(picking_ids),))
                self.env.cr.execute("DELETE FROM sale_order WHERE id in %s", (tuple(order_ids),))  
        if self.purchase_transfer:
            purchase_ids = self.env.cr.execute("""SELECT id,name FROM purchase_order""")
            purchase_order_ids = self.env.cr.fetchall()
            purchase_order_id = []
            purchase_order_name = []
            for pur_order_id in purchase_order_ids:
                purchase_order_id.append(pur_order_id[0])
                purchase_order_name.append(pur_order_id[1])
            if purchase_order_id:
                picking_query_exe = self.env.cr.execute("SELECT id FROM stock_picking WHERE origin in %s", (tuple(purchase_order_name),))
                picking_ids_fetchall = self.env.cr.fetchall()
                picking_ids = []
                for picking_id in picking_ids_fetchall:
                    picking_ids.append(picking_id[0])
                if picking_ids:
                    move_query_exe = self.env.cr.execute("SELECT id FROM stock_move WHERE picking_id in %s", (tuple(picking_ids),))
                    move_ids_fetchall = self.env.cr.fetchall()
                    move_ids = []
                    for move_id in move_ids_fetchall:
                        move_ids.append(move_id[0])
                    if move_ids:
                        move_line_query_exe = self.env.cr.execute("SELECT id FROM stock_move_line WHERE move_id in %s", (tuple(move_ids),))
                        move_line_ids_fetchall = self.env.cr.fetchall()
                        move_line_ids = []
                        for move_line_id in move_line_ids_fetchall:
                            move_line_ids.append(move_line_id[0])
                        if move_line_ids:
                            self.env.cr.execute("DELETE FROM stock_move_line WHERE id in %s", (tuple(move_line_ids),))
                        self.env.cr.execute("DELETE FROM stock_move WHERE id in %s", (tuple(move_ids),))
                    self.env.cr.execute("DELETE FROM stock_picking WHERE id in %s", (tuple(picking_ids),))
                self.env.cr.execute("DELETE FROM purchase_order WHERE id in %s", (tuple(purchase_order_id),))
        if self.only_transfers:
            sto_picking_ids = self.env.cr.execute("""SELECT id FROM stock_picking""")
            stock_picking_id = self.env.cr.fetchall()
            picking_ids = []
            for picking_id in stock_picking_id:
                picking_ids.append(picking_id[0])
            if picking_ids:
                move_query_exe = self.env.cr.execute("SELECT id FROM stock_move WHERE picking_id in %s", (tuple(picking_ids),))
                move_ids_fetchall = self.env.cr.fetchall()
                move_ids = []
                for move_id in move_ids_fetchall:
                    move_ids.append(move_id[0])
                if move_ids:
                    move_line_query_exe = self.env.cr.execute("SELECT id FROM stock_move_line WHERE move_id in %s", (tuple(move_ids),))
                    move_line_ids_fetchall = self.env.cr.fetchall()
                    move_line_ids = []
                    for move_line_id in move_line_ids_fetchall:
                        move_line_ids.append(move_line_id[0])
                    if move_line_ids:
                        self.env.cr.execute("DELETE FROM stock_move_line WHERE id in %s", (tuple(move_line_ids),))
                    self.env.cr.execute("DELETE FROM stock_move WHERE id in %s", (tuple(move_ids),))
                self.env.cr.execute("DELETE FROM stock_picking WHERE id in %s", (tuple(picking_ids),))
        if self.invoicing_payments_journal_entries:
            self.env.cr.execute("DELETE FROM account_partial_reconcile")
            self.env.cr.execute("DELETE FROM account_payment_term")
            self.env.cr.execute("DELETE FROM payment_acquirer")
            self.env.cr.execute("DELETE FROM payment_transaction")
            self.env.cr.execute("DELETE FROM payment_icon")
            self.env.cr.execute("DELETE FROM account_payment")
            self.env.cr.execute("DELETE FROM account_move")
        if self.only_journal_entries:
            self.env.cr.execute("DELETE FROM account_partial_reconcile")
            self.env.cr.execute("DELETE FROM account_move")
        if self.customers_vendors:
            self.env.cr.execute("DELETE FROM account_payment_register")
            res_users_execute = self.env.cr.execute("""SELECT partner_id FROM res_users""")
            res_users_fetchall = self.env.cr.fetchall()
            res_company_execute = self.env.cr.execute("""SELECT partner_id FROM res_company""")
            res_company_fetchall = self.env.cr.fetchall()
            delete_apart_ids = []
            for user_id in res_users_fetchall:
                delete_apart_ids.append(user_id[0])
            for company_id in res_company_fetchall:
                delete_apart_ids.append(company_id[0])
            self.env.cr.execute("DELETE FROM purchase_order WHERE partner_id not in %s", (tuple(delete_apart_ids),))
            self.env.cr.execute("DELETE FROM account_move_line WHERE partner_id not in %s", (tuple(delete_apart_ids),))
            self.env.cr.execute("DELETE FROM account_move WHERE partner_id not in %s", (tuple(delete_apart_ids),))
            self.env.cr.execute("DELETE FROM sale_order WHERE partner_id not in %s", (tuple(delete_apart_ids),))
            self.env.cr.execute("DELETE FROM res_partner WHERE id not in %s", (tuple(delete_apart_ids),))
        if self.accounts_ccounting:
            self.env.cr.execute("DELETE FROM account_partial_reconcile")
            self.env.cr.execute("DELETE FROM account_bank_statement")
            self.env.cr.execute("DELETE FROM account_payment")
            self.env.cr.execute("DELETE FROM account_move")
            self.env.cr.execute("DELETE FROM account_journal")
            self.env.cr.execute("DELETE FROM account_fiscal_position")
            self.env.cr.execute("DELETE FROM account_fiscal_position_tax")
            self.env.cr.execute("DELETE FROM account_incoterms")
            self.env.cr.execute("DELETE FROM account_reconcile_model")
            tax_id = self.env.cr.execute("""SELECT id FROM account_tax""")    
            tax_fetch = self.env.cr.fetchall()  
            tax = []
            for tax_fetchs in tax_fetch:
                tax.append(tax_fetchs[0])
            if tax:
                self.env.cr.execute("DELETE FROM account_tax WHERE id in %s", (tuple(tax),))
            accounts_id = self.env.cr.execute("""SELECT id FROM account_account""")    
            accounts_fetch = self.env.cr.fetchall()  
            accounts = []
            for accounts_fetchs in accounts_fetch:
                accounts.append(accounts_fetchs[0])
            if accounts:    
                self.env.cr.execute("DELETE FROM account_account WHERE id in %s", (tuple(accounts),))