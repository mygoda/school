# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.teacher.views import TeacherIndexView, ConnectParentsView
from applications.teacher.route.message import urlpatterns as message_url
from applications.teacher.route.term import urlpatterns as term_url
from applications.teacher.route.schedule import urlpatterns as schedule_url

urlpatterns = patterns('',
    url(r'^index/$', TeacherIndexView.as_view(), name='teacher_index_view'),
    url(r'^handle/evaluation/$', ConnectParentsView.as_view(), name='teacher_handle_evaluation_view'),
    url(r'^')
)

urlpatterns += message_url

urlpatterns += term_url

urlpatterns += schedule_url