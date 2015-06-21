# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.db import models
from django.conf import settings
from applications.teacher.models.subjects import SubjectsTemplate
from applications.teacher.models.schoolClass import SchoolClass
from libs.datetimes import datetime_now

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'user.User')


class Term(models.Model):
    class Meta:
        app_label = 'grade'
        db_name = 'grade_term_tpl'
        verbose_name = verbose_name_plural = "考试"

    NORMAL_TEST = 0
    MIDDLE_TEST = 1
    END_TEXT = 2

    TEXT_LIST = (
        (NORMAL_TEST, u'普通测验'),
        (MIDDLE_TEST, u'期中考试'),
        (END_TEXT, u'期末考试'),
    )

    name = models.CharField(u'考试名', max_length=128, blank=True, null=True)
    type = models.CharField(u'考试类型', max_length=128, choices=TEXT_LIST, default=NORMAL_TEST)
    subject = models.ForeignKey(SubjectsTemplate, verbose_name=u'科目', null=True, blank=True)
    school_class = models.ForeignKey(SchoolClass, verbose_name=u'班级', null=True, blank=True)

    created_at = models.DateTimeField(u'创建时间', default=datetime_now(), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

