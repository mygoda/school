# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.api.route.teacher import urlpatterns as teacher_url
from applications.api.route.student import urlpatterns as student_url

urlpatterns = patterns('',
)

urlpatterns += student_url

urlpatterns += teacher_url
