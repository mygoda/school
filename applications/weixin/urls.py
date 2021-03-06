# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.weixin import const
from applications.weixin.views import WeiXinResponseView, WeiXinDetailView, WeixinOAuthRedirectView

urlpatterns = patterns('',
    url(r'^callback/$', WeiXinResponseView.as_view(), name="weixin_response_view"),
    url(r'^texts/%s/$' % const.URL_ID, WeiXinDetailView.as_view(), name="weixin_detail_view"),
    url(r'^oauth2/redirect/$', WeixinOAuthRedirectView.as_view(), name="weixin_oauth_redirect_view")
)
