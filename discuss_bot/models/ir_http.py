# -*- coding: utf-8 -*-


from odoo import models


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(Http, self).session_info()
        if self.env.user.has_group('base.group_user'):
            res['discussbot_initialized'] = self.env.user.discussbot_state not in [False, 'not_initialized']
        return res
