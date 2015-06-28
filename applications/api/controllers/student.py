# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.views.generic import View
from applications.api.service.mixins.views import ApiCatchExceptionMixin, ApiQuerysetMixin
from applications.api.service.student import StudentsClassService, StudentsGradeService


class StudentQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return StudentsClassService(**kwargs)


#查看学生成绩接口
class StudentGradeQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return StudentsGradeService(**kwargs)