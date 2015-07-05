# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, View
from django.template import RequestContext
from applications.students.models import Students
from applications.students.models.evaluation import StudentEvaluation
from applications.teacher.models.teacher import Teacher, Term
from django.contrib.auth.decorators import login_required
from libs.http import json_success_response

#教师主页
class TeacherIndexView(View):
    from django.utils.decorators import method_decorator

    @method_decorator(login_required())
    def get(self, request, *args, **kwargs):
        template_name = 'teacher_v2/teacher_index.html'
        user = request.user
        is_teacher = Teacher.objects.filter(user_id=user.id).exists()
        if is_teacher:
            teacher = Teacher.objects.get(user_id=user.id)
            #目前评分是写死的
            grade = 5

            context = {
                'id': teacher.id,
                "username": teacher.user.username,
                "image": teacher.user.avatar,
                "subject": teacher.subject.name,
                "grade": grade,
            }
            return render_to_response(template_name, context)
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
    template_name = 'teacher_v2/teacher_class_all.html'

    def get_context_data(self, **kwargs):

        teacher = kwargs.get('id', '')

        return {
            "teacher": teacher
        }


 #返回班级主页
class TeacherClassDetailView(View):

    def get(self, request, *args, **kwargs):
        t = 'teacher_v2/teacher_class_detail.html'

        school_class_id = kwargs.pop('id', '')


        context = {
            "school_class": school_class_id,
        }

        return render_to_response(t, context)


#返回班级学生列表页
class TeacherClassStudentsView(View):

    def get(self, request, *args, **kwargs):
        t = 'teacher_v2/class_students_list.html'

        class_id = kwargs.pop('school_class_id', '')


        context = {
            "class_id": class_id,
        }

        return render_to_response(t, context)