# -*- coding: utf-8 -*-
# __author__ = xutao
from __future__ import division, unicode_literals, print_function
from django.shortcuts import render_to_response
from django.views.generic import View, TemplateView
from applications.statistics.models import TermStatistics


class TermStatisticsView(View):

    def get(self, request, *args, **kwargs):
        t = 'teacher_v2/teacher_term_statistics.html'
        term = kwargs.get('id', '')
        try:
            statistics = TermStatistics.objects.get(term_id=term)
        except TermStatistics.DoesNotExist:
            statistics = None

        context = {
            "statistics": statistics.to_json(),
            "term": term,
        }

        return render_to_response(t, context)