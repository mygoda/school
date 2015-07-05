# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.db import models
from django.conf import settings
from applications.teacher.models.schoolClass import SchoolClass
from applications.teacher.models.subjects import SubjectsTemplate
from applications.teacher.models.teacher import Term
from libs.datetimes import datetime_now

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'user.User')


class Students(models.Model):
    class Meta:
        app_label = 'students'
        db_table = 'students_students'
        verbose_name = verbose_name_plural = "学生"

    user = models.ForeignKey(auth_user_model, verbose_name=u'学生', blank=True, null=True)
    school_class = models.ForeignKey(SchoolClass, verbose_name=u'班级', blank=True, null=True)

    created_at = models.DateTimeField(u'创建时间', default=datetime_now(), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.user.username)

    def get_grade_with_term(self, term):
        grades = self.studentgrade_set.all()
        grade = grades.filter(term_id=term)
        return grade


class StudentGrade(models.Model):
    class Meta:
        app_label = 'students'
        db_table = 'students_students_grade'
        verbose_name = verbose_name_plural = "学生成绩"

    student = models.ForeignKey(Students, verbose_name=u'学生', blank=True, null=True)
    term = models.ForeignKey(Term, verbose_name=u'考试', blank=True, null=True)
    grade = models.IntegerField(u'成绩', blank=True, null=True)
    position = models.IntegerField(u'排名', blank=True, null=True)

    created_at = models.DateTimeField(u'创建时间', default=datetime_now(), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)


class StudentHomework(models.Model):
    class Meta:
        app_label = 'students'
        db_table = 'students_students_work'
        verbose_name = verbose_name_plural = "学生作业"

    school_class = models.ForeignKey(SchoolClass, verbose_name=u'班级', blank=True, null=True)
    subject = models.ForeignKey(SubjectsTemplate, verbose_name=u'科目', blank=True, null=True)
    content = models.CharField(u'作业内容', max_length=5536, blank=True, null=True)

    created_at = models.DateTimeField(u'创建时间', default=datetime_now(), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.school_class)
