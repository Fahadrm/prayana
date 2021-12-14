# -*- coding: utf-8 -*-


import time
import logging
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'


    @api.onchange('date_done')
    def _onchange_effective_date(self):

        for picking in self:
            if picking.move_lines:
                for move in picking.move_lines:
                    if move._origin.id:
                        value = move._origin.id
                    elif move.id:
                        value = move.id
                    moves = self.env['account.move'].search([('stock_move_id','=',value)])
                    for i in moves:
                        date_value = picking.date_done.date() if picking.date_done else " "
                        i.write({'date' : date_value})
        return

            # s=1


# class StockMove(models.Model):
#     _inherit = "stock.move"
#
#     def _create_account_move_line(self, credit_account_id, debit_account_id, journal_id, qty, description, svl_id,
#                                    cost):
#          self.ensure_one()
#          AccountMove = self.env['account.move'].with_context(default_journal_id=journal_id)
#
#          move_lines = self._prepare_account_move_line(qty, cost, credit_account_id, debit_account_id, description)
#          if move_lines:
#              if self.picking_id.date_done:
#                  date = datetime.strptime(str(self.picking_id.date_done), '%Y-%m-%d %H:%M:%S')
#              else:
#                  date = self._context.get('force_period_date', fields.Date.context_today(self))
#          # if move_lines:
#          #     date = self._context.get('force_period_date', fields.Date.context_today(self))
#              new_account_move = AccountMove.sudo().create({
#                  'journal_id': journal_id,
#                  'line_ids': move_lines,
#                  'date': date,
#                  'ref': description,
#                  'stock_move_id': self.id,
#                  'stock_valuation_layer_ids': [(6, None, [svl_id])],
#                  'move_type': 'entry',
#              })
#              new_account_move._post()
#
#
