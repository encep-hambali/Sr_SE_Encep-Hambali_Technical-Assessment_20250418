{
    'name' : 'HB Pemesanan Ruangan',
    'version' : '14',
    'websiete': '-',
    'author' : 'Hambali IT',

    'category' : 'module custom',
    'descriptionn' : '-',





    'depends' : ['base'],
    'data' : [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/pemesanan_sequence.xml',
        'data/data_default_master_ruangan.xml',
        'views/master_ruangan_view.xml',
        'views/pemesanan_ruangan_view.xml'
              ],

    'installable' : True,
    'application' :True,
    'auto-install' : False
}