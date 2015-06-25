# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.api.controllers.teacher import TeacherMessageQuerysetView, \
    TeacherTermsQuerysetView, TeacherSchedulesView
from settings.const import URL_ID, TEACHER_ID


urlpatterns = patterns('',
    url(r'^%s/messages/$' % TEACHER_ID, TeacherMessageQuerysetView.as_view(), name='teacher_messages_queryset_view'),
    url(r'^%s/terms/$' % TEACHER_ID, TeacherTermsQuerysetView.as_view(), name='teacher_terms_queryset_view'),
    url(r'^%s/schedules/$' % TEACHER_ID, TeacherSchedulesView.as_view(), name='teacher_schedules_queryset_view')
)