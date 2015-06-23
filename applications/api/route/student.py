# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.api.controllers.student import StudentQuerysetView

urlpatterns = patterns('',
    url(r'^students/filter/$', StudentQuerysetView.as_view(), name='students_queryset_view'),
)