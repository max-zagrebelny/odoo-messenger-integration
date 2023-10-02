# Copyright 2021 Eugene Molotov <https://github.com/em230418>
# Copyright 2022 Ivan Yelizariev <https://twitter.com/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).

import json
import logging

import requests
from requests import request as rq
from twilio.rest import Client
from odoo import _, api, models, http


from odoo.addons.multi_livechat.tools import get_multi_livechat_eval_context
from odoo.addons.sync.models.sync_project import AttrDict
from odoo.addons.sync.tools import LogExternalQuery

_logger = logging.getLogger(__name__)


class SyncProjectWhatsApp(models.Model):

    _inherit = "sync.project.context"

    @api.model
    def _eval_context_whatsapp_chatapi(self, secrets, eval_context):
        """Adds whatsapp object:"""
        params = eval_context["params"]

        if not params.WHATSAPP_CHATAPI_API_URL:
            raise Exception(_("WhatsApp Chat API URL is not set"))

        if not secrets.WHATSAPP_CHATAPI_TOKEN:
            raise Exception(_("WhatsApp Chat API token is not set"))

        account_sid = params.WHATSAPP_CHATAPI_API_URL
        auth_token = secrets.WHATSAPP_CHATAPI_TOKEN
        client = Client(account_sid, auth_token)

        # Створення вебхука
        # webhook = client.incoming_phone_numbers('WhatsApp:+1234567890') \
        #     .update(
        #     sms_url='https://ваш_сервер.com/twilio/webhook',
        #     sms_method='POST'
        # )
        # def whatsapp_service_request(method, url, data=None):
        #     r = request(
        #         method,
        #         params.WHATSAPP_CHATAPI_API_URL.rstrip("/")
        #         + url
        #         + "?token="
        #         + secrets.WHATSAPP_CHATAPI_TOKEN,
        #         json=data,
        #         timeout=5,
        #     )
        #     r.raise_for_status()
        #     return r

        # @LogExternalQuery("WhatsApp->set_webhook", eval_context)
        # def set_webhook(url):
        #     return whatsapp_service_request(
        #         "post", "/webhook", {"set": True, "webhookUrl": url}
        #     )

        @LogExternalQuery("WhatsApp->send_message", eval_context)
        def send_message(from_user, to, body):
            message = client.messages.create(
                body=body,
                from_=from_user,
                to=to
            )
            return message.sid

        multi_livechat_context = AttrDict(
            get_multi_livechat_eval_context(
                self.env, "multi_livechat_whatsapp", eval_context
            )
        )

        def whatsapp_webhook_parse(request):
            data = dict(http.Request(request).get_http_params())
            return data

        whatsapp_service_api = AttrDict(
            {
                # "set_webhook": set_webhook,
                "send_message": send_message,
                # "send_file": send_file,
            }
        )

        return {
            "whatsapp_service_api": whatsapp_service_api,
            "whatsapp_webhook_parse": whatsapp_webhook_parse,
            "multi_livechat": multi_livechat_context,
        }
