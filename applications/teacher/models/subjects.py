# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.db import models
from libs.datetimes import datetime_now


class SubjectsTemplate(models.Model):
    class Meta:
        app_label = u"teacher"
        db_table = u'teacher_subjects_tpl'
        verbose_name = verbose_name_plural = u"课程模板"

    name = models.CharField(u'课程名', max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(u'创建时间', default=datetime_now(), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

