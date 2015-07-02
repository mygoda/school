# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from applications.teacher.models.teacher import Teacher
from libs.datetimes import datetime_now
from django.db import models
from django.conf import settings

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'user.User')


class TeacherSchedule(models.Model):
    class Meta:
        app_label = u"teacher"
        db_table = u'teacher_teacher_schedule'
        verbose_name = verbose_name_plural = u"教师课程"

    teacher = models.ForeignKey(Teacher, verbose_name=u'教师', blank=True, null=True)
    week = models.IntegerField(u'时间', null=True, blank=True)
    start = models.IntegerField(u'课程开始时间', blank=True, null=True)
    end = models.IntegerField(u'课程结束时间', blank=True, null=True)
    position = models.CharField(u'地点', blank=True, null=True, max_length=128)
    content = models.CharField(u'内容', blank=True, null=True, max_length=2528)

    created_at = models.DateTimeField(u'创建时间', blank=True, null=True, default=datetime_now())

    def __unicode__(self):
        return self.id