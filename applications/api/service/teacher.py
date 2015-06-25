# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from applications.api.service.base import ServiceBase
from applications.teacher.models.message import TeacherMessage
from applications.teacher.models.schedule import TeacherSchedule
from applications.teacher.models.teacher import SchoolClassTeacherShip


class TeacherMessageService(ServiceBase):
    model = TeacherMessage

    queryset_name = "teacherMessages"
    obj_name = "teacherMessage"

    def obj_to_json(self, obj):
        return {
            "id": obj.id,
            "content": obj.content,
            "type": obj.type,
            "created_date": obj.get_date,
            "created_time": obj.get_time
        }


class TeacherScheduleService(ServiceBase):

    model = TeacherSchedule

    queryset_name = 'schedules'

    obj_name = 'schedule'

    def obj_to_json(self, obj):
        return {
            "id": obj.id,
            "time": obj.time,
            "start": obj.start,
            "end": obj.end,
            "position": obj.position
        }

