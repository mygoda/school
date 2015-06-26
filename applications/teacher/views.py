# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.template import RequestContext
from applications.students.models.evaluation import StudentEvaluation
from applications.teacher.models.teacher import Teacher
from django.contrib.auth.decorators import login_required
from libs.http import json_success_response

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


#处理老师评价学生的处理接口
class ConnectParentsView(View):
    def post(self, request, *args, **kwargs):
        content = request.POST.get('content', '')
        teacher_id = Teacher.objects.get(user_id=request.user.id).id
        student = request.POST.get('student', '')

        evaluation = StudentEvaluation(student_id=student, content=content, teacher_id=teacher_id)
        evaluation.save()

        return json_success_response(json_data={})

#渲染写评价给家长的页面
class WriteToParentsView(TemplateView):
    template_name = "message/write_content.html"


#教师班级列表页
class TeacherClassesView(TemplateView):
    t = 'classes_list.html'

