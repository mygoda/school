# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from libs.datetimes import datetime_now
from django.db import models
from django.conf import settings

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'user.User')


class SchoolClass(models.Model):
    class Meta:
        app_label = u"teacher"
        db_table = u'teacher_school_class'
        verbose_name = verbose_name_plural = u"班级"

    grade = models.IntegerField(u'年级', blank=True, null=True)
    team = models.IntegerField(u'班', blank=True, null=True)
    number = models.IntegerField(u'班级人数', blank=True, null=True)

    created_at = models.DateTimeField(u'创建时间', blank=True, null=True, default=datetime_now())

    def __unicode__(self):
        return u"%s年%s班" % (self.grade, self.team)

    @classmethod
    def rise_grade(cls):
        all_class = cls.objects.all()
        for item in all_class:
            item.grade += 1
            item.save()



