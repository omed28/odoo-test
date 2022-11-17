from odoo import api, fields, models, _

class WorkOrder(models.Model):
    _name = 'work.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Work Order'
    _rec_name = 'wo_number'

    wo_number = fields.Char(string='Work Order Number', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    booking_reference = fields.Many2one('sale.order',  domain="[('state','in',['sale','done'])]", string='Booking Reference', required=True, no_create=True)
    team_id = fields.Many2one('service.team', string='Team', required=True)
    team_leader = fields.Many2one('res.users', string='Team Leader', required=True)
    team_members = fields.Many2many('res.users', string='Team Members', required=True)
    planned_start = fields.Date(string='Planned Start', required=True)
    planned_end = fields.Date(string='Planned End', required=True)
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Date End')
    amount_total = fields.Float(string='Total Amount')
    state = fields.Selection([('pending', 'Pending'), ('in_progress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')], string='State', default='pending')
    note = fields.Text(string='Note')

    @api.onchange('booking_reference')
    def _onchange_booking_reference(self):
        self.amount_total = self.booking_reference.amount_total

    @api.onchange('team_id')
    def _onchange_team_id(self):
        self.team_leader = self.team_id.team_leader
        self.team_members = self.team_id.team_members

    @api.model
    def create(self, vals):
        if vals.get('wo_number', _('New')) == _('New'):
            vals['wo_number'] = self.env['ir.sequence'].next_by_code('work.order') or _('New')
        result = super(WorkOrder, self).create(vals)
        return result

    def start_work(self):
        self.state = 'in_progress'
        self.date_start = fields.Date.today()

    def end_work(self):
        self.state = 'done'
        self.date_end = fields.Date.today()

    def reset_work(self):
        self.state = 'pending'
        self.date_start = False
        self.date_end = False

    def print_work_order(self):
        return self.env.ref('booking_order_santomifitrada_111122.work_order_report').report_action(self)
    
    def cancel_work(self):
        return {
            'name': _('Cancel Work Order'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'cancel.work.order',
            'target': 'new',
            'context': {'default_work_order': self.id},
        }