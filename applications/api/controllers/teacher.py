# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.shortcuts import render_to_response
from django.views.generic import View
from applications.api.service.teacher import TeacherMessageService, TeacherScheduleService
from applications.api.service.mixins.views import ApiCatchExceptionMixin, ApiQuerysetMixin, ApiGetMixin
from applications.api.service.term import TeacherTermService, TermsQuerysetService, QuerysetStudentByTermService
from applications.teacher.models.teacher import SchoolClassTeacherShip


class TeacherMessageQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherMessageService(**kwargs)


class TeacherTermsQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherTermService(**kwargs)


#返回教师所属班级
class TeacherClassesQuerysetView(View):
    def get(self, request, *args, **kwargs):
        t = 'teacher_classes.html'
        classes = SchoolClassTeacherShip.objects.filter(**kwargs)
        classes_json = map(lambda obj: obj.school_class.to_json(), classes)
        context = {
            "classes": classes_json,
        }

        return render_to_response(t, context)


class TeacherSchedulesView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherScheduleService(**kwargs)


class ClassTermsQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TermsQuerysetService(**kwargs)


class ClassStudentsQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return QuerysetStudentByTermService(**kwargs)




        

