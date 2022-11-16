from odoo import api, fields, models

class JadwalPelajaran(models.Model):
    _name = "jadwal.pelajaran"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Jadwal Pelajaran"
    _rec_name = "kode_jadwal"

    kode_jadwal = fields.Char(string="Kode Jadwal")
    hari = fields.Selection([('senin','Senin'),('selasa','Selasa'),('rabu','Rabu'),('kamis','Kamis'),('jumat','Jumat'),('sabtu','Sabtu')], string="Hari")
    kelas_id = fields.Many2one(comodel_name="data.kelas", string="Kelas")
    mata_pelajaran_id = fields.Many2one(comodel_name="mata.pelajaran", string="Mata Pelajaran")
    durasi = fields.Integer(string="Durasi", help="Durasi mata pelajaran dalam menit")
