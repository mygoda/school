# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
import json
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, View
from django.template import RequestContext
from applications.grade.models.term import Term
from applications.statistics.models.terms import TermStatistics
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
    template_name = 'term_detail.html'

    def get_context_data(self, **kwargs):
        return {
            "term": self.request.GET.get('term', '')
        }




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


#老师录入成绩的保存处理,处理成功返回200，跳转会考试管理的主页, 并且进行相关的统计操作
class HandleStudentsGrade(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body).get('data', '')
        data = sorted(data, key=lambda x:x['grade'], reverse=True)
        term = request.POST.get('term', '')
        position = 1
        max_grade = data[0].get('grade', '')
        pass_number = 0
        excellent_number = 0
        sum = 0
        for item in data:
            point = item.get('grade', '')
            grade = StudentGrade(student_id=item.get('id', ''), term_id=term, grade=point, position=position)
            grade.save()
            if point > 60:
                pass_number += 1
            elif point > 90:
                excellent_number += 1
            sum += point
            position += 1
        self.statictics(sum=sum, pass_number=pass_number, max=max_grade, excellent_number=excellent_number, term=term)
        return json_success_response(json_data={})

    def statictics(self, sum, pass_number, excellent_number, term, max):
        term_statistics = TermStatistics(term_id=term, sum=sum, pass_number=pass_number, excellent_number=excellent_number, max=max)
        term_statistics.save()


class GetRecordStudentsGradeView(TemplateView):
    template_name = 'record_students_grade.html'

    def get_context_data(self, **kwargs):
        school_class = self.request.GET.get('school_class', '')

        context = {
            "school_class": school_class
        }
        return RequestContext(self.request, context)


