# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.teacher.controllers.term import TeacherCreateTermView

urlpatterns = patterns('',
    url(r'^create/term/$', TeacherCreateTermView.as_view(), name='teacher_create_view'),
)