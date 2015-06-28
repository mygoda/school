# -*- coding: utf-8 -*-
# __author__ = xutao

from django.db import models
from applications.grade.models.term import Term
from libs.datetimes import datetime_now


class TermStatistics(models.Model):
    class Meta:
        app_label = 'statistics'
        db_table = 'statistics_term'
        verbose_name = verbose_name_plural = u"考试统计"

    term = models.ForeignKey(Term, verbose_name=u'考试', null=True, blank=True)
    sum = models.IntegerField(u'总分', null=True, blank=True)
    max = models.IntegerField(u'最高分', null=True, blank=True)
    pass_number = models.IntegerField(u'及格人数', null=True, blank=True)
    excellent_number = models.IntegerField(u'优秀人数', null=True, blank=True)

    created_at = models.DateTimeField(u'创建时间', blank=True, null=True, default=datetime_now())

    def __unicode__(self):
        return self.id

    def to_json(self):
        return {
            "id": self.id,
            "sum": self.sum,
            "max": self.max,
            "pass_number": self.pass_number,
            "excellent_number": self.excellent_number,
        }