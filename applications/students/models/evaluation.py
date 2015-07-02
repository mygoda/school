# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.db import models
from django.conf import settings
from applications.students.models.students import Students
from applications.teacher.models.teacher import Teacher
from libs.datetimes import datetime_now

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'user.User')



class StudentEvaluation(models.Model):
    class Meta:
        app_label = 'students'
        db_table = 'students_student_evaluation'
        verbose_name = verbose_name_plural = u"学生评价"

    student = models.ForeignKey(Students, verbose_name=u'学生', null=True, blank=True)
    content = models.CharField(u'评价内容', max_length=5536, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name=u'评价人', null=True, blank=True)

    created_at = models.DateTimeField(u'创建时间', default=datetime_now(), blank=True, null=True)

    def __unicode__(self):
        return self.id