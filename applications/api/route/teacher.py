# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.api.controllers.teacher import TeacherMessageQuerysetView, \
    TeacherTermsQuerysetView, TeacherSchedulesQuerysetView, TeacherClassesQuerysetView, ClassTermsQuerysetView, ClassStudentsQuerysetView, \
    TeacherTermDetailView, TeacherLoginView
from settings.const import URL_ID, TEACHER_ID, CLASS_ID, TYPE


urlpatterns = patterns('',
    url(r'^teacher/%s/messages/$' % TEACHER_ID, TeacherMessageQuerysetView.as_view(), name='teacher_messages_queryset_view'),
    url(r'^teacher/%s/terms/$' % TEACHER_ID, TeacherTermsQuerysetView.as_view(), name='teacher_terms_queryset_view'),
    url(r'^teacher/%s/schedules/$' % TEACHER_ID, TeacherSchedulesQuerysetView.as_view(), name='teacher_schedules_queryset_view'),
    url(r'^teacher/%s/classes/$' % TEACHER_ID, TeacherClassesQuerysetView.as_view(), name='teacher_classes_queryset_view'),
    url(r'^teacher/class/%s/terms/$' % CLASS_ID, ClassTermsQuerysetView.as_view(), name='class_terms_queryset_view'),
    url(r'^teacher/class/%s/type/%s/$' % (CLASS_ID, TYPE), ClassTermsQuerysetView.as_view(), name='class_type_terms_queryset_view'),
    url(r'^teacher/class/%s/students/$' % CLASS_ID, ClassStudentsQuerysetView.as_view(), name='class_students_queryset_view'),
    url(r'^teacher/term/%s/detail/$' % URL_ID, TeacherTermDetailView.as_view(), name='teacher_term_detail_view'),
    url(r'^teacher/login/$', TeacherLoginView.as_view(), name='teacher_login_view'),
)