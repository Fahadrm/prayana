import base64
import binascii
import codecs
import collections
import unicodedata
from odoo import api, fields, models


class LeadInherit(models.Model):

    _inherit = "crm.lead"

    @api.model
    def default_get(self, values):
        res = super(LeadInherit, self).default_get(values)
        res.update({
            'user_id':int(self.env['ir.config_parameter'].sudo().get_param('custom_crm.user_id')) or False
                    })
        imp = self.env['base_import.import']
        return res


