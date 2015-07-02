# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.api.controllers.student import StudentQuerysetView
from settings.const import CLASS_ID

urlpatterns = patterns('',
    url(r'^/class/%s/students/$' % CLASS_ID, StudentQuerysetView.as_view(), name='class_students_queryset_view'),
)