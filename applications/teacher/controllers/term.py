# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
import json
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, View
from django.template import RequestContext
from applications.statistics.models.terms import TermStatistics
from applications.students.models.students import StudentGrade, Students
from applications.teacher.models.teacher import Teacher, TeacherTermShip, SchoolClassTeacherShip, Term
from libs.http import json_success_response
from django.contrib.auth.decorators import login_required


class TeacherTermsView(TemplateView):
    template_name = 'teacher_v2/teacher_terms_list.html'

    def get_context_data(self, **kwargs):
        context = {
            "teacher": kwargs.pop('id', '')
        }
        return RequestContext(self.request, context)


#对于某个考试相关的详情页，应该查看该考试相关的统计页面
class TeacherTermDetailView(TemplateView):
    template_name = 'term_detail.html'

    def get_context_data(self, **kwargs):
        return {
            "term": self.request.GET.get('term', '')
        }


class TeacherCreateTermSuccessView(View):

    def get(self, request, *args, **kwargs):
        t = 'teacher_v2/create_term_success.html'
        school_class = request.GET.get('school_class', '')
        term = request.GET.get('term', '')

        context = {
            'school_class': school_class,
            'term': term,
        }

        return render_to_response(t, context)


class TeacherCreateTermView(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        teacher = data.get('teacher', '')
        term = self.create_term(data=data, teacher=teacher)
        self.create_term_teacher_ship(teacher=teacher, term=term)
        context = {
            "school_class": data.get('school_class', ''),
            "term": term.id
        }
        return json_success_response(json_data=context)

    def create_term(self, data, teacher):
        term_name = data.get('name', '')
        school_class = data.get('school_class', '')
        subject = Teacher.objects.get(id=teacher).subject_id
        term_type = data.get('type', '')

        term = Term(name=term_name, type=term_type, subject_id=subject, school_class_id=school_class)
        term.save()
        return term

    def create_term_teacher_ship(self, teacher, term):
        teacher_term_ship = TeacherTermShip(teacher_id=teacher, term_id=term.id)
        teacher_term_ship.save()


    def get(self, request, *args, **kwargs):

        template = 'teacher_v2/teacher_create_term.html'
        teacher = request.GET.get('teacher', '')
        context = {
            "teacher": teacher
        }
        return render_to_response(template, context)


#老师录入成绩的保存处理,处理成功返回200，跳转会考试管理的主页, 并且进行相关的统计操作
class HandleStudentsGradeView(View):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        data = body.get('data', '')
        data = sorted(data, key=lambda x: x['grades'], reverse=True)
        term = body.get('term', '')
        position = 1
        max_grade = int(data[0].get('grades', ''))
        pass_number = 0
        excellent_number = 0
        sum = 0
        for item in data:
            point = int(item.get('grades', ''))
            grade = StudentGrade(student_id=item.get('id', ''), term_id=term, grade=point, position=position)
            grade.save()
            if point > 60:
                pass_number += 1
            elif point > 90:
                excellent_number += 1
            sum += point
            position += 1
        average = sum/len(data)
        self.statictics(sum=sum, pass_number=pass_number, max=max_grade, excellent_number=excellent_number, term=term, average=average)
        return json_success_response(json_data={"term": term})

    def statictics(self, sum, pass_number, excellent_number, term, max, average):
        term_statistics = TermStatistics(term_id=term, sum=sum, pass_number=pass_number, excellent_number=excellent_number, max=max, average=average)
        term_statistics.save()


class GetRecordStudentsGradeView(TemplateView):
    template_name = 'teacher_v2/teacher_record_score.html'

    def get_context_data(self, **kwargs):
        school_class = self.request.GET.get('school_class', '')
        term = self.request.GET.get('term', '')
        context = {
            "school_class": school_class,
            'term': term,
        }
        return RequestContext(self.request, context)


class RecordGradeSuccessView(TemplateView):

    template_name = 'teacher_v2/teacher_create_score_success.html'

    def get_context_data(self, **kwargs):
        term = self.request.GET.get('term')

        context = {
            "term": term
        }

        return RequestContext(self.request, context)


class TermFilterByTypeView(View):

    def get(self, request, *args, **kwargs):
        t = 'teacher_v2/class_test_list.html'
        type_list = Term.TEXT_LIST
        type = int(request.GET.get('type', ''))
        title = type_list[type][1]

        context = {
            "title": title,
            "type": type,
            "school_class": kwargs.get('id', '')
        }

        return render_to_response(t, context)


