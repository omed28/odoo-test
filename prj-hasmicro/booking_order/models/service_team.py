from odoo import models, fields, api, _

class ServiceTeam(models.Model):
    _name = 'service.team'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Service Team'
    _rec_name = 'team_name'
    _order = 'team_name'

    team_name = fields.Char(string='Team Name', required=True)
    team_leader = fields.Many2one('res.users', string='Team Leader', required=True)
    team_members = fields.Many2many('res.users', string='Team Members', required=True)

