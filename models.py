# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class PartnerRequest(models.Model):
    _inherit = "asterisk_plus.call",

    requests = fields.Many2many('request.request', inverse_name='call_id', required=True)

    def _get_all_requests(self):
        cr = self.pool.cursor()
        all_requests = self.env['request.request'].search(cr, self.env.uid, [])
        lines = []
        for i in all_requests:
            if i.request_id:
                data = {
                    "request_id": i.id,
                }
                lines.append((0, 0, data))
        self.requests = self.lines
        return self.requests

