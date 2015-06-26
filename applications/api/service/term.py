# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from applications.api.service.base import ServiceBase
from applications.grade.models.term import Term
from applications.students.models.students import Students
from applications.teacher.models.teacher import TeacherTermShip


class TeacherTermService(ServiceBase):
    model = TeacherTermShip

    queryset_name = 'terms'

    obj_name = 'term'

    def obj_to_json(self, obj):
        return {
            "id": obj.id,
            "name": obj.term.name,
            "type": obj.term.type,
            "subject": obj.subject,
            "school_class": obj.term.school_class,
        }


#录入成绩时获取学生列表
class QuerysetStudentByTermService(ServiceBase):
    model = Students

    queryset_name = 'students'

    obj_name = 'student'

    def obj_to_json(self, obj):
        return {
            "id": obj.id,
            "username": obj.user.username
        }


class TermsQuerysetService(ServiceBase):
    model = Term

    queryset_name = 'terms'

    obj_name = 'term'

    def obj_to_json(self, obj):
        return {
            "id": obj.id,
            "name": obj.name,
            "subject": obj.subject,
            "teacher": obj.created_by_id
        }
