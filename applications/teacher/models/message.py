# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from applications.teacher.models.teacher import Teacher
from libs.datetimes import datetime_now, datetime_to_str
from django.db import models
from django.conf import settings

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'user.User')


class TeacherMessage(models.Model):
    class Meta:
        app_label = u"teacher"
        db_table = u'teacher_message'
        verbose_name = verbose_name_plural = u"教师通知"

    SCHOOL = 0
    PARENTS = 1
    SYSTEM = 2
    MESSAGE_TYPE = (
        (SCHOOL, u'学校'),
        (PARENTS, u'家长'),
        (SYSTEM, u'系统')
    )

    content = models.CharField(u'通知内容', max_length=2578, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name=u'接受者', null=True, blank=True)
    type = models.SmallIntegerField(u'类型', default=SCHOOL, choices=MESSAGE_TYPE)

    created_at = models.DateTimeField(u'创建时间', blank=True, null=True, default=datetime_now())

    def __unicode__(self):
        return unicode(self.teacher.user.username)

    @property
    def get_date(self):
        return datetime_to_str(self.created_at, "%Y-%m-%d")

    @property
    def get_time(self):
        return datetime_to_str(self.created_at, "%H:%M")

    def get_created_at(self):
        return datetime_to_str(self.created_at, "%Y-%m-%d %H:%M")

    def to_json(self):
        return {
            "id": self.id,
            "created_by": self.created_by_id,
            "created_at": self.get_created_at(),
            "content": self.content,
        }

