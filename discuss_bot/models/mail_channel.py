# -*- coding: utf-8 -*-


from odoo import api, models, _


class Channel(models.Model):
    _inherit = 'mail.channel'

    def execute_command_help(self, **kwargs):
        super().execute_command_help(**kwargs)
        self.env['mail.bot']._apply_logic(self, kwargs, command="help")  # kwargs are not usefull but...

    @api.model
    def init_discussbot(self):
        if self.env.user.discussbot_state in [False, 'not_initialized']:
            discussbot_id = self.env['ir.model.data']._xmlid_to_res_id("base.partner_root")
            channel_info = self.channel_get([discussbot_id])
            channel = self.browse(channel_info['id'])
            message = _("Hello,<br/>Odoo's chat helps employees collaborate efficiently. I'm here to help you discover its features.<br/><b>Try to send me an emoji</b> <span class=\"o_discussbot_command\">:)</span>")
            channel.sudo().message_post(body=message, author_id=discussbot_id, message_type="comment", subtype_xmlid="mail.mt_comment")
            self.env.user.discussbot_state = 'onboarding_emoji'
            return channel
