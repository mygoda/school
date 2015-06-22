# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.template import RequestContext
from applications.teacher.models.teacher import Teacher
from django.contrib.auth.decorators import login_required


#教师主页
class TeacherIndexView(TemplateView):
    template_name = 'teacher_index.html'

    @login_required
    def get_context_data(self, **kwargs):
        user = self.request.user
        is_teacher = Teacher.objects.filter(user_id=user.id).exists()
        if is_teacher:
            teacher = Teacher.objects.get(user_id=user.id)
            #目前评分是写死的
            grade = 5

            context = {
                "username": teacher.user.username,
                "image": teacher.user.avatar,
                "subject": teacher.subject.name,
                "grade": grade,
            }
            return RequestContext(self.request, context)
        return HttpResponseRedirect('/login/error/')