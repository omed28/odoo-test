from odoo import api, fields, models

class DataGuru(models.Model):
    _name = "data.guru"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Data Guru"
    _rec_name = "nama_guru"

    nip = fields.Char(string="NIP")
    nama_guru = fields.Char(string="Nama Guru")
    foto_guru = fields.Binary(string="Foto Guru")
    jenis_kelamin = fields.Selection([('laki-laki','Laki-Laki'),('perempuan','Perempuan')], string="Jenis Kelamin")
    tempat_lahir = fields.Char(string="Tempat Lahir")
    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    agama = fields.Selection([('islam','Islam'),('kristen','Kristen'),('katolik','Katolik'),('hindu','Hindu'),('budha','Budha')], string="Agama")
    alamat = fields.Text(string="Alamat")
    no_telp = fields.Char(string="No Telp")
    mata_pelajaran_id = fields.Many2one(comodel_name="mata.pelajaran", string="Mata Pelajaran")