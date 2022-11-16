{
    'name': "Matrica School",
    'version': '13.0.1.0',
    'category': 'School',
    'summary': 'Matrica',
    'author': 'Santomi Fitrada',
    'website': 'http://prabusolusimedia.com',
    'description': """
        - Custom School Module 
    """,
    'depends': [
      'base','mail',
    ],
    
    'data': [
        'security/ir.model.access.csv',
        'views/school_views.xml',
        'views/kelas_views.xml',
        'views/siswa_views.xml',
        'views/guru_views.xml',
        'views/mapel_views.xml',
        'views/ruangan_views.xml',
        'views/jurusan_views.xml',
        'views/pelajaran_views.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3' 
}
