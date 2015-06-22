# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.shortcuts import render_to_response
from django.views.generic import View
from libs.http import json_success_response
from applications.api.service.teacher import TeacherMessageService
from applications.api.service.mixins.views import ApiCatchExceptionMixin, ApiQuerysetMixin, ApiGetMixin
from applications.api.service.term import TeacherTermService
from applications.grade.models.term import Term
from applications.teacher.models.teacher import TeacherTermShip, SchoolClassTeacherShip, Teacher


class TeacherMessageQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherMessageService(**kwargs)


class TeacherMessageDetailView(ApiCatchExceptionMixin, ApiGetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherMessageService(**kwargs)


class TeacherTermQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherTermService(**kwargs)


class TeacherTermDetailView(ApiCatchExceptionMixin, ApiGetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherTermService(**kwargs)


class TeacherCreateTermView(View):
    #教师创建考试页面

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

    def get(self, request, *args, **kwargs):

        template = 'create_term.html'

        user = request.user
        classes = SchoolClassTeacherShip.objects.filter(teacher_id=user.id)

        classes_json = map(lambda obj: obj.to_json(), classes)
        context = {
            "classes": classes_json
        }
        return render_to_response(template, context)

        

