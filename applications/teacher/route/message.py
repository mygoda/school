# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.teacher.controllers.message import TeacherMessageDetailView, TeacherMessagesView
from settings.const import URL_ID

urlpatterns = patterns('',
    url(r'^messages/$', TeacherMessagesView.as_view(), name='teacher_messages_view'),
    url(r'^message/%s/$' % URL_ID, TeacherMessageDetailView.as_view(), name='teacher_message_view')

)