# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from applications.api.service.base import ServiceBase
from applications.students.models.students import Students


#通过班级查找班级学生
class StudentsClassService(ServiceBase):
    model = Students

    queryset_name = 'students'

    obj_name = 'student'

    def obj_to_json(self, obj):
        return {
            "id": obj.id,
            "name": obj.user.username,
        }

