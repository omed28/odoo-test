from odoo import api, fields, models

class DataSiswa(models.Model):
    _name = "data.siswa"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Data Siswa"
    _rec_name = "nama_siswa"

    nis = fields.Char(string="NIS")
    nama_siswa = fields.Char(string="Nama Siswa")
    foto_siswa = fields.Binary(string="Foto Siswa")
    jenis_kelamin = fields.Selection([('laki-laki','Laki-Laki'),('perempuan','Perempuan')], string="Jenis Kelamin")
    tempat_lahir = fields.Char(string="Tempat Lahir")
    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    agama = fields.Selection([('islam','Islam'),('kristen','Kristen'),('katolik','Katolik'),('hindu','Hindu'),('budha','Budha')], string="Agama")
    alamat = fields.Text(string="Alamat")
    nama_ayah = fields.Char(string="Nama Ayah")
    nama_ibu = fields.Char(string="Nama Ibu")
    no_telp = fields.Char(string="No Telp")
    usia = fields.Integer(string="Usia")
