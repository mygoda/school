# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django import template
from applications.weixin.models import App

register = template.Library()


@register.inclusion_tag('weixin/config.html')
def weixin_config(request, nonce_str="", timestamp="", app=None):
    if not app:
        app = App.only_one()

    host = request.META.get("HTTP_HOST", "")
    path = request.path
    query_string = request.META.get("QUERY_STRING", "")

    if query_string:
        url = "http://%s%s?%s" % (host, path, query_string)
    else:
        url = "http://%s%s" % (host, path)

    sign = app.sign(url, nonce_str, timestamp)
    return {
        "sign": sign
    }

