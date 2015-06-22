# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView, View
from django.template import RequestContext


class TeacherTermsView(TemplateView):
    template_name = 'term/list.html'

    def get_context_data(self, **kwargs):
        return RequestContext(self.request)

