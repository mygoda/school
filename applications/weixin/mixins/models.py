# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from urllib import quote_plus
from applications.weixin.const import JS_API_LIST
from applications.weixin.weixin.utils import to_weixin_xml, dict_to_xml
from libs.datetimes import datetime_delta, datetime_now, datetime_to_str
from django.conf import settings
from libs.hashs import md5

import hashlib
import random
import string

import requests
import json
import time
from libs.uuids import get_code


class AppWeixinMixin(object):
    expires_seconds = 4000

    def refresh_access_token(self):
        base_url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": self.app_key,
            "secret": self.app_id,
        }

        content = requests.get(base_url, params=params).content
        json_data = json.loads(content)
        self.access_token = json_data['access_token']
        access_token_expire_in = datetime_delta(datetime_now(), seconds=self.expires_seconds)
        self.token_expires_in = access_token_expire_in
        self.save()

    def get_access_token(self):
        if not any([self.app_key, self.app_id]):
            raise Exception(u"必须申请app_key和app_secret".encode("utf-8"))
        if datetime_now() <= self.token_expires_in:
            return self.access_token
        self.refresh_access_token()
        return self.access_token

    def refresh_jsapi(self):
        base_url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket"
        access_token = self.get_access_token()
        params = {
            "access_token": access_token,
            "type": "jsapi",
        }
        content = requests.get(base_url, params=params).content
        json_data = json.loads(content)
        ticket = json_data['ticket']
        self.jsapi_ticket = ticket
        ticket_expire_in = datetime_delta(datetime_now(), seconds=self.expires_seconds)
        self.ticket_expires_in = ticket_expire_in
        self.save()

    def get_jsapi_ticket(self):
        if not any([self.app_key, self.app_id]):
            raise Exception(u"必须申请app_key和app_secret".encode("utf-8"))
        if datetime_now() <= self.ticket_expires_in:
            return self.jsapi_ticket
        self.refresh_jsapi()
        return self.jsapi_ticket

    @classmethod
    def __create_nonce_str(cls):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    @classmethod
    def __create_timestamp(cls):
        return int(time.time())

    def sign(self, url, nonce_str="", timestamp=""):
        jsapi_ticket = self.get_jsapi_ticket()
        ret = {
            'nonceStr': self.__create_nonce_str() if not nonce_str else nonce_str,
            'jsapi_ticket': jsapi_ticket,
            'timestamp': self.__create_timestamp() if not timestamp else timestamp,
            'url': url,
        }
        s = '&'.join(['%s=%s' % (key.lower(), ret[key]) for key in sorted(ret)])
        ret['signature'] = hashlib.sha1(s).hexdigest()
        ret['appId'] = self.app_key
        ret['jsApiList'] = JS_API_LIST
        ret['debug'] = True
        return ret

    @classmethod
    def __sign(cls, secret_key, **kwargs):
        s = []
        for key in sorted(kwargs):
            if kwargs[key]:
                s.append('%s=%s' % (key, kwargs[key]))
        s.append("key=%s" % secret_key)
        temp_s = "&".join(s)
        md5_s = md5(temp_s.encode("utf-8"))
        return md5_s.upper()