{
    'name' : 'Custom CRM',
    'version' : '1.1',
    'summary': 'Customer Relationship',
    'sequence': 1,
    'description': "This Is A Customer Relationship Software",
    'category': 'crm',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['crm', 'base'],
    'data': [
        
        # 'data/crm_sequence_data.xml',
        
        # 'views/custom_crm_view.xml',
        'views/res_config_settings_view.xml'
       
     

    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
