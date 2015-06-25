# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, View
from applications.teacher.models.schedule import TeacherSchedule


class TeacherScheduleDetailView(View):
    #查看日程的详细内容,带上该日程的id
    def get(self, request, *args, **kwargs):
        t = 'schedule_detail.html'
        schedule = TeacherSchedule.objects.get(**kwargs)
        context = {
            "content": schedule.content
        }
        return render_to_response(t, context, context_instance=RequestContext(request))


#日程信息通过接口去获得
class TeacherSchedulesView(TemplateView):
    template_name = 'schedules_list.html'