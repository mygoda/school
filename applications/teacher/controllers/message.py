# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView, View
from django.template import RequestContext
from applications.students.models.evaluation import StudentEvaluation
from libs.http import json_success_response


class GetTeacherMessage(TemplateView):
    template_name = 'message/teacher_index.html'

    def get_context_data(self, **kwargs):
        return RequestContext(self.request)


#处理老师评价学生的处理接口
class ConnectParentsView(View):
    def post(self, request, *args, **kwargs):
        content = request.POST.get('content', '')
        teacher_id = request.POST.get('teacher', '')
        student = request.POST.get('student', '')

        evaluation = StudentEvaluation(student_id=student, content=content, teacher_id=teacher_id)
        evaluation.save()

        return json_success_response(json_data={})


