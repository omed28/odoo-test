from odoo import api, fields, models

class RuangKelas(models.Model):
    _name = "ruang.kelas"
    _description = "Ruang Kelas"
    _rec_name = "nama_ruangan"

    nama_ruangan = fields.Char(string="Nama Ruangan")
    kapasitas = fields.Integer(string="Kapasitas")
