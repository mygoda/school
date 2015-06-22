# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.views.generic import View
from applications.api.service.teacher import TeacherMessageService
from applications.api.service.mixins.views import ApiCatchExceptionMixin, ApiQuerysetMixin, ApiGetMixin


class TeacherMessageQuerysetView(ApiCatchExceptionMixin, ApiQuerysetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherMessageService(**kwargs)


class TeacherMessageDetailView(ApiCatchExceptionMixin, ApiGetMixin, View):
    def get_model_service(self, **kwargs):
        return TeacherMessageService(**kwargs)