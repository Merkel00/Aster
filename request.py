from datetime import datetime, timedelta
from odoo import models, fields, api


class RequestEvent(models.Model):
    _name = 'asterisk_plus.call_request'
    _inherit = 'asterisk_plus.call',
    _description = 'Request Event'

    call_id = fields.Many2one('asterisk_plus.call', ondelete='cascade')
    request_date = fields.Date('Created')
    request_name = fields.Many2one('request.request')

    # @api.depends("request_id")
    # def _compute_request_id(self):
    #     for rec in self:
    #         rec.request_id = False
    #         rec.request_date = False
    #         if rec.request_id:
    #             rec.request_name = rec.request_id.name
    #             rec.request_date = rec.stage_id.date_created
