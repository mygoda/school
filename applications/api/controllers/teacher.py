# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.shortcuts import render_to_response
from django.views.generic import View
from applications.api.service.teacher import TeacherMessageService, TeacherScheduleService, TeacherClassesService
from applications.api.service.mixins.views import ApiCatchExceptionMixin, ApiQuerysetMixin, ApiGetMixin
from applications.api.service.term import TeacherTermService, TermsQuerysetService, QuerysetStudentByTermService, \
    TermStatisticsService
from applications.teacher.models.teacher import SchoolClassTeacherShip


class TeacherMessageQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherMessageService(**kwargs)


class TeacherTermsQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherTermService(**kwargs)


#返回教师所属班级
class TeacherClassesQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherClassesService(**kwargs)


class TeacherSchedulesQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherScheduleService(**kwargs)


class ClassTermsQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TermsQuerysetService(**kwargs)


class ClassStudentsQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return QuerysetStudentByTermService(**kwargs)


class TeacherTermDetailView(ApiCatchExceptionMixin, ApiGetMixin, View):
    def get_model_service(self, **kwargs):
        return TermStatisticsService(**kwargs)




        

