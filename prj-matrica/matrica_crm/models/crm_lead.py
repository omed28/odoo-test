from odoo import api, fields, models

class Lead(models.Model):
    _inherit = "crm.lead"


    new_customer = fields.Boolean(string="New Customer ?", default=False)
    segmen_customer = fields.Selection([('konstruksi','Konstruksi'),('perbankan','Perbankan'),('pemerintah','Pemerintah'),('bumd/bumn','BUMD/BUMN'),('kementerian','Kementerian'),('swasta','Swasta'),('lainnya','Lainnya')], string="Segmen Customer")
    segmen_product_id = fields.Many2one(comodel_name="segmen.product", string="Segmen Product")
    task_progress_ids = fields.One2many(comodel_name="task.progress", inverse_name="lead_id", string="Task Progress")

class TaskProgress(models.Model):
    _name = "task.progress"

    lead_id = fields.Many2one(comodel_name="crm.lead", string="Lead")
    name = fields.Char(string="Task")
    deadline = fields.Date(string="Deadline")
    progress = fields.Selection([('todo','To Do'),('inprogress','In Progress'),('done','Done')], string="Progress")
    note = fields.Text(string="Note")


    