# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.db import models
from django.conf import settings
from django_extensions.db.fields.json import JSONField
from libs.datetimes import datetime_now

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'user.User')


class WeixinPayLog(models.Model):
    class Meta:
        app_label = "weixin"
        db_table = "weixin_log"
        verbose_name = verbose_name_plural = u"微信支付日志"

    created_by = models.ForeignKey(auth_user_model, verbose_name=u"操作用户",
                                   default=None, blank=True, null=True, related_name=u"create_orders")
    created_at = models.DateTimeField(u"创建时间", default=datetime_now)

    pre_unifiedorder = JSONField()
    unifiedorder_data = JSONField()

    def __unicode__(self):
        return unicode(self.id)