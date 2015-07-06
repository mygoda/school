# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.statistics.views import TermStatisticsView
from settings.const import URL_ID

urlpatterns = patterns('',
    url(r'^term/%s/$' % URL_ID, TermStatisticsView.as_view(), name='term_statistics_view'),
)