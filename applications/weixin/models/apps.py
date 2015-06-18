# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.db import models
from applications.weixin.mixins.models import AppWeixinMixin
from libs.datetimes import datetime_now
from libs.models.models import SingletonModel
from django.conf import settings
from libs.uuids import get_uuid
import requests
import json


class App(SingletonModel, AppWeixinMixin):
    class Meta:
        app_label = "weixin"
        db_table = "weixin_app"
        verbose_name_plural = verbose_name = u"账号设置"

    name = models.CharField("微信名", max_length=64, default="", blank=True, null=True)
    app_url = models.CharField("微信回调地址", max_length=256, blank=True, null=True)
    app_token = models.CharField("微信Token", max_length=64, blank=True, null=True)

    app_key = models.CharField("app_id", max_length=64, blank=True, null=True)
    app_id = models.CharField("app_secret", max_length=64, blank=True, null=True)

    mch_id = models.CharField(u"商户id", max_length=64, blank=True, null=True, default="")
    mch_secret = models.CharField(u"商户密钥", max_length=128, blank=True, null=True, default="")

    access_token = models.CharField(u"access_token", max_length=256, blank=True, null=True, default="")
    token_expires_in = models.DateTimeField(u"token过期时间", default=datetime_now, blank=True, null=True)

    jsapi_ticket = models.CharField("jsapi_ticket", max_length=256, blank=True, null=True, default="")
    ticket_expires_in = models.DateTimeField(u"ticket过期时间", default=datetime_now, blank=True, null=True)

    def __unicode__(self):
        return bool(self.name) and self.name or self.owner.email

    @property
    def subscribe_rule(self):
        subscribe = self.subscribeitem_set.all()
        if not subscribe.count():
            return None
        else:
            return subscribe[0].rule

    def get_app_url(self):
        return "%s/weixin/callback/" % settings.APP_HOST_NAME

    def save(self, force_insert=False, force_update=False, using=None):
        if force_insert and force_update:
            raise ValueError("Cannot force both insert and updating in model saving.")

        if not self.app_url:
            self.app_url = self.get_app_url()
        if not self.app_token:
            self.app_token = get_uuid()

        if self.app_key and self.app_id:
            self.delete_menus()
            self.create_menus()

        super(App, self).save(force_insert, force_update, using)

    def create_menus(self):
        from applications.weixin.models.menus import MenuItem
        token = self.get_access_token()
        post_dict = MenuItem.get_menus_by_app(self)
        headers = {'content-type': 'application/json'}

        url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % token
        return requests.post(url, data=json.dumps(post_dict, ensure_ascii=False).encode("utf-8"), headers=headers)

    def delete_menus(self):
        token = self.get_access_token()
        url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % token
        return requests.get(url)