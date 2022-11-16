from odoo import api, fields, models

class MataPelajaran(models.Model):
    _name = "mata.pelajaran"
    _description = "Mata Pelajaran"
    _rec_name = "nama_pelajaran"

    nama_pelajaran = fields.Char(string="Nama Pelajaran")
    bidang_studi_id = fields.Many2one(comodel_name="bidang.studi", string="Jurusan")
