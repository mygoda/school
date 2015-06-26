# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.api.controllers.teacher import TeacherMessageQuerysetView, \
    TeacherTermsQuerysetView, TeacherSchedulesView, TeacherClassesQuerysetView, ClassTermsQuerysetView, ClassStudentsQuerysetView
from settings.const import URL_ID, TEACHER_ID, CLASS_ID, TYPE


urlpatterns = patterns('',
    url(r'^%s/messages/$' % TEACHER_ID, TeacherMessageQuerysetView.as_view(), name='teacher_messages_queryset_view'),
    url(r'^%s/terms/$' % TEACHER_ID, TeacherTermsQuerysetView.as_view(), name='teacher_terms_queryset_view'),
    url(r'^%s/schedules/$' % TEACHER_ID, TeacherSchedulesView.as_view(), name='teacher_schedules_queryset_view'),
    url(r'^%s/classes/$' % TEACHER_ID, TeacherClassesQuerysetView.as_view(), name='teacher_classes_queryset_view'),
    url(r'^class/%s/terms/$' % CLASS_ID, ClassTermsQuerysetView.as_view(), name='class_terms_queryset_view'),
    url(r'^class/%s/type/%s/$' % (CLASS_ID, TYPE), ClassTermsQuerysetView.as_view(), name='class_type_terms_queryset_view'),
    url(r'^class/%s/students/$' % CLASS_ID, ClassStudentsQuerysetView.as_view(), name='class_students_queryset_view'),
)