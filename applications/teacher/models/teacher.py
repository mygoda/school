# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.db import models
from django.conf import settings
from applications.grade.models.term import Term
from applications.teacher.models.subjects import SubjectsTemplate
from applications.teacher.models.schoolClass import SchoolClass
from libs.datetimes import datetime_now

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'user.User')


class Teacher(models.Model):
    class Meta:
        app_label = u"teacher"
        db_table = u'teacher_teacher'
        verbose_name = verbose_name_plural = u"教师"

    user = models.ForeignKey(auth_user_model, verbose_name=u'教师名', null=True, blank=True)
    subject = models.ForeignKey(SubjectsTemplate, verbose_name=u'课程', null=True, blank=True)
    is_master = models.BooleanField(u'是否班主任', blank=True, null=True)

    created_at = models.DateTimeField(u'创建时间', blank=True, null=True, default=datetime_now())

    def __unicode__(self):
        return unicode(self.user.username)

    def get_master_class(self):
        if self.is_master:
            master_class = self.schoolclassteachership_set.all()
            return master_class[0]
        return False


class SchoolClassTeacherShip(models.Model):
    class Meta:
        app_label = u"teacher"
        db_table = u'teacher_teacher_ship'
        verbose_name = verbose_name_plural = u"教师班级关系"

    teacher = models.ForeignKey(Teacher, verbose_name=u'教师', blank=True, null=True)
    school_class = models.ForeignKey(SchoolClass, verbose_name=u'班级', blank=True, null=True)

    created_at = models.DateTimeField(u'创建时间', blank=True, null=True, default=datetime_now())


    def __unicode__(self):
        return self.id

    def to_json(self):
        return {
            "id": self.id,
            "class_name": self.school_class.__unicode__()
        }


class SchoolClassMasterShip(models.Model):
    class Meta:
        app_label = u"teacher"
        db_table = u'teacher_master_ship'
        verbose_name = verbose_name_plural = u"班主任"

    master = models.ForeignKey(Teacher, verbose_name=u'教师', null=True, blank=True)
    school_class = models.ForeignKey(SchoolClass, verbose_name=u'班级', blank=True, null=True)

    created_at = models.DateTimeField(u'创建时间', blank=True, null=True, default=datetime_now())


class TeacherTermShip(models.Model):
    class Meta:
        app_label = u"teacher"
        db_table = u'teacher_term_ship'
        verbose_name = verbose_name_plural = u"教师考试关系"

    teacher = models.ForeignKey(Teacher, verbose_name=u'教师', blank=True, null=True)
    term = models.ForeignKey(Term, verbose_name=u'考试', blank=True, null=True)

    created_at = models.DateTimeField(u'创建时间', blank=True, null=True, default=datetime_now())

    def __unicode__(self):
        return self.id


