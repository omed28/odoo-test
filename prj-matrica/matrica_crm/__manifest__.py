{
    'name': "Matrica CRM",
    'version': '13.0.1.0',
    'category': 'CRM',
    'summary': 'Matrica',
    'author': 'Santomi Fitrada',
    'website': 'http://prabusolusimedia.com',
    'description': """
        - Custom CRM Module 
    """,
    'depends': [
      'crm','sales_team',
    ],
    
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/segmen_product_views.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3' 
}
