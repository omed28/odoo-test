from odoo import api, fields, models

class BidangStudi(models.Model):
    _name = "bidang.studi"
    _description = "Bidang Studi"
    _rec_name = "nama_jurusan"

    nama_jurusan = fields.Char(string="Jurusan")
