# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
import json
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, View
from django.template import RequestContext
from applications.grade.models.term import Term
from applications.students.models.students import StudentGrade, Students
from applications.teacher.models.teacher import Teacher, TeacherTermShip, SchoolClassTeacherShip
from libs.http import json_success_response
from django.contrib.auth.decorators import login_required

class TeacherTermsView(TemplateView):
    template_name = 'term/list.html'

    def get_context_data(self, **kwargs):
        return RequestContext(self.request)


#对于某个考试相关的详情页，应该查看该考试相关的统计页面
class TeacherTermDetailView(TemplateView):
    pass



class TeacherCreateTermView(View):
    #教师创建考试页面
    @login_required
    def post(self, request, *args, **kwargs):
        t = 'create_success.html'
        data = request.POST
        user = request.user
        term = self.create_term(data=data)
        self.create_term_teacher_ship(user=user, term=term)
        context = {
            "school_class": data.get('school_class', ''),
            "term": term.id
        }
        return render_to_response(t, context)

    def create_term(self, data, user):
        term_name = data.get('name', '')
        school_class = data.get('school_class', '')
        subject = Teacher.objects.get(id=user.id).subject_id
        term_type = data.get('type', '')

        term = Term(name=term_name, type=term_type, subject_id=subject, school_class=school_class)
        term.save()
        return term

    def create_term_teacher_ship(self, user, term):
        teacher_term_ship = TeacherTermShip(teacher_id=user.id, term_id=term.id)
        teacher_term_ship.save()

    #处理获取填写考试信息的页面
    @login_required
    def get(self, request, *args, **kwargs):

        template = 'create_term.html'

        user = request.user
        classes = SchoolClassTeacherShip.objects.filter(teacher_id=user.id)

        classes_json = map(lambda obj: obj.to_json(), classes)
        context = {
            "classes": classes_json
        }
        return render_to_response(template, context)


#老师录入成绩的保存处理,处理成功返回200，跳转会考试管理的主页
class HandleStudentsGrade(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body).get('data', '')
        data = sorted(data, key=lambda x:x['grade'], reverse=True)
        term = request.POST.get('term', '')
        position = 1
        for item in data:
            grade = StudentGrade(student_id=item.get('id', ''), term_id=term, grade=item.get('grade', ''), position=position)
            grade.save()
            position += 1
        return json_success_response(json_data={})


class GetRecordStudentsGradeView(TemplateView):
    template_name = 'record_students_grade.html'

    def get_context_data(self, **kwargs):
        school_class = self.request.GET.get('school_class', '')

        context = {
            "school_class": school_class
        }
        return RequestContext(self.request, context)


