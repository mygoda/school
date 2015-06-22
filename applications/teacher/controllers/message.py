# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView
from django.template import RequestContext


class GetTeacherMessage(TemplateView):
    template_name = 'message/teacher_index.html'

    def get_context_data(self, **kwargs):
        return RequestContext(self.request)

