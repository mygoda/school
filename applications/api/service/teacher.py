# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from applications.api.service.base import ServiceBase
from applications.teacher.models import SchoolClassTeacherShip
from applications.teacher.models.message import TeacherMessage
from applications.teacher.models.schedule import TeacherSchedule


class TeacherMessageService(ServiceBase):
    model = TeacherMessage

    queryset_name = "teacherMessages"

    obj_name = "teacherMessage"

    def obj_to_json(self, obj):
        return {
            "id": obj.id,
            "content": obj.content,
            'type_id': obj.type,
            "type": obj.get_type_display(),
            "created_date": obj.get_date,
            "created_time": obj.get_created_at(),
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


    #返回教师所属班级
class TeacherClassesService(ServiceBase):
    model = SchoolClassTeacherShip

    queryset_name = 'teacher_classes'

    obj_name = 'teacher_class'

    def obj_to_json(self, obj):
        return {
            "id": obj.id,
            "class_name": obj.school_class.__unicode__()
        }
