from odoo import api, fields, models

class SegmenProduct(models.Model):
    _name = "segmen.product"
    _description = "Segmen Product"
    _rec_name = "name"

    name = fields.Char(string="Segmen Product")
