# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.api.controllers.teacher import TeacherSchedulesView
from applications.teacher.controllers.schedule import TeacherScheduleDetailView
from settings.const import TEACHER_ID, URL_ID


urlpatterns = patterns('',
    url(r'%s/schedules/$' % TEACHER_ID, TeacherSchedulesView.as_view(), name="teacher_get_schedules_view"),
    url(r'^schedule/%s/detail' % URL_ID, TeacherScheduleDetailView.as_view(), name="teacher_get_schedule_detail_view"),
)