# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from applications.api.models import UserPassword
from applications.users.models import User
from libs.http import json_success_response, json_error_response
import json
from django.views.generic import View
from applications.api.service.teacher import TeacherMessageService, TeacherScheduleService, TeacherClassesService
from applications.api.service.mixins.views import ApiCatchExceptionMixin, ApiQuerysetMixin, ApiGetMixin
from applications.api.service.term import TeacherTermService, TermsQuerysetService, QuerysetStudentByTermService, \
    TermStatisticsService
from applications.teacher.models.teacher import SchoolClassTeacherShip, Teacher


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


class TeacherLoginView(View):

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        phone = body.get('phone', '')
        password = body.get('password', '')
        passed = UserPassword.check_password(password, phone)
        print('yes')
        if not passed:
            return json_error_response(msg=u'密码错误')

        user = User.get_user_by_phone(phone)

        if not user:
            return json_error_response(msg=u'没有该用户')

        if not Teacher.objects.filter(user_id=user.id).exists():
            return json_error_response(msg=u"对不起，你不是老师！")

        user = authenticate(phone=phone)
        print(user)
        login(request, user)

        return json_success_response(json_data={})



        

