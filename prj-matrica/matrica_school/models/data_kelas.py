from odoo import api, fields, models
from odoo.exceptions import ValidationError

class DataKelas(models.Model):
    _name = "data.kelas"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Data Kelas"
    _rec_name = "nama_kelas"

    nama_kelas = fields.Char(string="Nama Kelas")
    foto_kelas = fields.Binary(string="Foto Kelas")
    ruang_kelas = fields.Many2one('ruang.kelas', string="Ruang Kelas")
    kapasitas_kelas = fields.Integer(string="Kapasitas Kelas", related="ruang_kelas.kapasitas")
    ketua_kelas = fields.Many2one(comodel_name="data.siswa", string="Ketua Kelas")
    wakil_ketua_kelas = fields.Many2one(comodel_name="data.siswa", string="Wakil Ketua Kelas")
    bendahara_kelas = fields.Many2one(comodel_name="data.siswa", string="Bendahara Kelas")
    wali_kelas = fields.Many2one(comodel_name="data.guru", string="Wali Kelas")
    siswa_ids = fields.One2many(comodel_name="anggota_kelas", inverse_name="kelas_id", string="Siswa")

    # @api.onchange('ruang_kelas')
    # def _onchange_ruang_kelas(self):
    #     if self.ruang_kelas:
    #         self.kapasitas_kelas = self.ruang_kelas.kapasitas

class AnggotaKelas(models.Model):
    _name = "anggota_kelas"
    _description = "Anggota Kelas"
    _rec_name = "siswa_id"

    siswa_id = fields.Many2one(comodel_name="data.siswa", string="Siswa")
    kelas_id = fields.Many2one(comodel_name="data.kelas", string="Kelas")
    nis = fields.Char(string="NIS", related="siswa_id.nis")
    jenis_kelamin = fields.Selection([('laki-laki','Laki-Laki'),('perempuan','Perempuan')], string="Jenis Kelamin", related="siswa_id.jenis_kelamin")
    tempat_lahir = fields.Char(string="Tempat Lahir", related="siswa_id.tempat_lahir")
    tanggal_lahir = fields.Date(string="Tanggal Lahir", related="siswa_id.tanggal_lahir")
    agama = fields.Selection([('islam','Islam'),('kristen','Kristen'),('katolik','Katolik'),('hindu','Hindu'),('budha','Budha')], string="Agama", related="siswa_id.agama")
    no_telp = fields.Char(string="No Telp", related="siswa_id.no_telp")

    @api.onchange('siswa_id')
    def _onchange_siswa_id(self):
        for rec in self:           
            if rec.kelas_id.kapasitas_kelas < len(rec.kelas_id.siswa_ids)-1:
                raise ValidationError("Kapasitas kelas sudah penuh")

            siswa_ids = self.env['anggota_kelas'].search([('siswa_id','=',rec.siswa_id.id)])
            if siswa_ids:
                raise ValidationError("Siswa sudah terdaftar di kelas lain")






