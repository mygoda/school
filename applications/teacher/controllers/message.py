# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView, View
from django.template import RequestContext
from applications.teacher.models.message import TeacherMessage


class TeacherMessagesView(TemplateView):
    template_name = 'teacher_v2/teacher_messages_list.html'

    def get_context_data(self, **kwargs):
        teacher = kwargs.pop('id', '')
        context = {
            "teacher": teacher
        }
        return RequestContext(self.request, context)


class TeacherMessageDetailView(TemplateView):
    template_name = 'teacher_v2/teacher_message_detail.html'

    def get_context_data(self, **kwargs):
        message = TeacherMessage.objects.get(**kwargs)
        context = message.to_json()
        return RequestContext(self.request, context)



