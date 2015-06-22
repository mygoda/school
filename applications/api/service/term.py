# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from applications.api.service.base import ServiceBase
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
            "school_class": obj.term.school_class,
        }