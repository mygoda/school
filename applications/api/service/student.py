# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from applications.api.service.base import ServiceBase
from applications.students.models.students import Students, StudentGrade


#通过班级查找班级学生
class StudentsClassService(ServiceBase):
    model = Students

    queryset_name = 'students'

    obj_name = 'student'

    def obj_to_json(self, obj):
        return {
            "id": obj.id,  #学生id
            "name": obj.user.username,
        }


class StudentsGradeService(ServiceBase):
    model = StudentGrade

    queryset_name = 'students_grade'

    obj_name = 'student_grade'

    order_by = '-grade'

    def obj_to_json(self, obj):
        return {
            "student": obj.student_id,
            "name": obj.student.user.username,
            "term": obj.term_id,
            "grade": obj.grade,
            "position": obj.position,
        }