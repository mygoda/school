# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView, View
from django.template import RequestContext
from applications.teacher.models.message import TeacherMessage


class TeacherMessagesView(TemplateView):
    template_name = 'message_list.html'

    def get_context_data(self, **kwargs):
        return RequestContext(self.request)


class TeacherMessageDetailView(TemplateView):
    template_name = 'message_detail.html'

    def get_context_data(self, **kwargs):
        message = TeacherMessage.objects.get(**kwargs)
        context = message.to_json()
        return RequestContext(self.request, context)



