# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.db import models
from django.db.models import Q
from django.utils.http import urlquote_plus
from applications.weixin.models import App
from libs.datetimes import datetime_now, datetime_delta
from django.conf import settings
import requests

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'user.User')


class WeixinUserToken(models.Model):
    class Meta:
        app_label = "weixin"
        db_table = "weixin_user_token"
        verbose_name_plural = verbose_name = u"微信用户token"

    user = models.OneToOneField(auth_user_model, verbose_name=u"会员", default=None, blank=True, null=True, unique=True)
    openid = models.CharField(u"openid", max_length=128, blank=True, null=True, default="", unique=True)
    access_token = models.CharField(u"access_token", max_length=256, blank=True, null=True, default="")
    refresh_token = models.CharField(u"refresh_token", max_length=256, blank=True, null=True, default="")
    scope = models.CharField(u"scope", max_length=256, blank=True, null=True, default="")

    expires_in = models.DateTimeField(u"过期时间", default=datetime_now, blank=True, null=True)
    created_at = models.DateTimeField(u"创建时间", default=datetime_now, blank=True, null=True)

    def __unicode__(self):
        return self.openid

    @classmethod
    def generate_authorize_url(cls, redirect_uri, scope="snsapi_userinfo", state="200", app=None):
        if not app:
            app = App.only_one()
        redirect_uri = urlquote_plus(redirect_uri)
        url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=%s" % (app.app_key, redirect_uri, scope, state )
        return url

    @classmethod
    def fetch_user_access_token(cls, user, code, app=None):
        if not app:
            app = App.only_one()
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (app.app_key, app.app_id, code)
        json_data = requests.get(url).json()
        expires_in = datetime_delta(datetime_now(), seconds=json_data['expires_in'])

        token = WeixinUserToken(user=user, openid=json_data['openid'], access_token=json_data['access_token'],
                                refresh_token=json_data['refresh_token'], scope=json_data['scope'],
                                expires_in=expires_in)
        token.save()

    @classmethod
    def get_or_update_token(cls, user, access_token_json):
        openid = access_token_json['openid']

        # 先找用户是否已经绑定
        try:
            token = cls.objects.get(user=user)
        except:
            token = None

        # 如果没有绑定，查看微信号是否绑定过用户，再没有，创建用户
        if not token:
            try:
                token = cls.objects.get(openid=openid)
            except cls.DoesNotExist:
                token = cls(user=user)

        token.user = user
        token.openid = openid
        token.access_token = access_token_json['access_token']
        token.refresh_token = access_token_json['refresh_token']
        token.scope = access_token_json['scope']
        token.expires_in = datetime_delta(datetime_now(), seconds=3600)
        token.save()
        return token

    @classmethod
    def fetch_access_json(cls, code, app=None):
        if not app:
            app = App.only_one()
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (app.app_key, app.app_id, code)
        json_data = requests.get(url).json()
        return json_data

    @classmethod
    def get_token_by_openid(cls, openid):
        try:
            token = cls.objects.get(openid=openid)
            return token
        except cls.DoesNotExist:
            return None

    def refresh_access_token(self, app=None):
        if not app:
            app = App.only_one()
        url = "https://api.weixin.qq.com/sns/oauth2/refresh_token?appid=%s&grant_type=refresh_token&refresh_token=%s" % (app.app_key, self.refresh_token)
        json_data = requests.get(url).json()

        expires_in = datetime_delta(datetime_now(), seconds=json_data['expires_in'])
        self.expires_in = expires_in
        self.access_token = json_data['access_token']
        self.refresh_token = json_data['refresh_token']
        self.openid = json_data['openid']
        self.scope = json_data['scope']
        self.save()

    def get_user_info(self):
        url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s" % (self.access_token, self.expires_in)
        json_data = requests.get(url).json()
        return json_data