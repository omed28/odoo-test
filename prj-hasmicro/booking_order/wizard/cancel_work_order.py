from odoo import api, fields, models

class CancelWorkOrder(models.TransientModel):
    _name = 'cancel.work.order'
    _description = 'Cancel Work Order'

    cancel_reason = fields.Text(string='Cancel Reason', required=True)

    def cancel_work_order(self):
        active_id = self.env.context.get('active_id')
        work_order = self.env['work.order'].browse(active_id)
        work_order.state = 'cancelled'
        work_order.note = self.cancel_reason
        return True