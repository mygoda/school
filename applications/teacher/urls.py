# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.teacher.views import TeacherIndexView
from applications.teacher.route.message import urlpatterns as message_url

urlpatterns = patterns('',
    url(r'index/', TeacherIndexView.as_view(), name='teacher_index_view'),
)

urlpatterns += message_url