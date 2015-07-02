# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.contrib import admin
from applications.statistics.models.terms import TermStatistics

class TermStatisticsAdmin(admin.ModelAdmin):
    pass

admin.site.register(TermStatistics, TermStatisticsAdmin)