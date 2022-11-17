from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    is_booking_order = fields.Boolean(string='Is Booking Order')
    service_team_id = fields.Many2one('service.team', string='Service Team', required=True)
    team_leader = fields.Many2one('res.users', string='Team Leader', required=True)
    team_members = fields.Many2many('res.users', string='Team Members', required=True)
    booking_start = fields.Date(string='Booking Start', required=True)
    booking_end = fields.Date(string='Booking End', required=True)

    @api.onchange('service_team_id')
    def _onchange_service_team_id(self):
        if self.service_team_id:
            self.team_leader = self.service_team_id.team_leader
            self.team_members = self.service_team_id.team_members

    def action_check_team(self):
        if self.is_booking_order:
            check_team = self.env['work.order'].browse(self.id).search([('team_id', '=', self.service_team_id.id) , ('state', '!=', 'cancel')])
            if check_team:
                for check_team in check_team:
                    if check_team.planned_start <= self.booking_start <= check_team.planned_end:
                        raise UserError(_('Team is not available for this time period on Sale Order %s') % check_team.booking_reference.name)
                    elif check_team.planned_start <= self.booking_end <= check_team.planned_end:
                        raise UserError(_('Team already has work order during that period on Sale Order %s') % check_team.booking_reference.name)
                    else :
                        raise UserError(_('Team is available for booking'))
            else :
                raise UserError(_('Team is available for booking'))
        else:
            return True

                
    def _get_wo_number(self, vals):
        if vals.get('wo_number', _('New')) == _('New'):
            vals['wo_number'] = self.env['ir.sequence'].next_by_code('work.order') or _('New')
        return vals

    def action_create_work_order(self):
        get_wo_number = self.env['ir.sequence'].next_by_code('work.order') or _('New')
        wo = self.env['work.order'].create({
            'wo_number': get_wo_number,
            'booking_reference': self.id,
            'team_id': self.service_team_id.id,
            'team_leader': self.team_leader.id,
            'team_members': [(6, 0, self.team_members.ids)],
            'planned_start': self.booking_start,
            'planned_end': self.booking_end,
            'amount_total': self.amount_total,
            'state': 'pending',
        })
        return wo

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if self.is_booking_order:
            check = self.env['work.order'].browse(self.id).search([('team_id', '=', self.service_team_id.id) , ('state', '!=', 'cancel')])
            if check:
                for check in check:
                    if check.planned_start <= self.booking_start <= check.planned_end:
                        raise UserError(_('Team is not available for this time period on Sale Order %s, Please booking another date') % check.booking_reference.name)
                    elif check.planned_start <= self.booking_end <= check.planned_end:
                        raise UserError(_('Team already has work order during that period on Sale Order %s, Please booking another date') % check.booking_reference.name)
                    else :
                        self.action_create_work_order()
            else :
                self.action_create_work_order()
        else:
            return True


    
