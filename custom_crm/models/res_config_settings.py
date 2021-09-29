from odoo import api, models, fields


class ResConfigSettingsInherit(models.TransientModel):   
     
    _inherit = 'res.config.settings'
    
    user_id = fields.Many2one('res.users', string="Sales Person", default_model='res.users')
    
    @api.model
    def get_values(self):
        res = super(ResConfigSettingsInherit, self).get_values()
        res.update(
            user_id=int(self.env['ir.config_parameter'].sudo().get_param('custom_crm.user_id'))) or False
        return res

    def set_values(self):
        res = super(ResConfigSettingsInherit, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('custom_crm.user_id', self.user_id.id)
        return res
        
            

        
