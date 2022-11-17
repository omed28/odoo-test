{
    'name': "Booking Order",
    'version': '13.0.1.0',
    'category': 'Sales',
    'summary': 'Hashmicro Booking Order',
    'author': 'Santomi Fitrada',
    'website': 'http://prabusolusimedia.com',
    'description': """
        - Custom Booking Order Module
    """,
    'depends': [
      'sale','mail',
    ],
    
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/service_team_views.xml',
        'views/booking_views.xml',
        'views/sale_views.xml',
        'views/work_order_views.xml',
        'views/menu_views.xml',
        'wizard/cancel_work_order_views.xml',
        'reports/work_order_report.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3' 
}
