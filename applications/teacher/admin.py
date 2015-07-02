# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.contrib import admin

from applications.teacher.models.teacher import Teacher, SchoolClassTeacherShip, SchoolClassMasterShip, TeacherTermShip
from applications.teacher.models.message import TeacherMessage
from applications.teacher.models.schedule import TeacherSchedule
from applications.teacher.models.schoolClass import SchoolClass
from applications.teacher.models.subjects import SubjectsTemplate


class TeacherAdmin(admin.ModelAdmin):
    pass


class TeacherTermShipAdmin(admin.ModelAdmin):
    pass


class SchoolClassTeacherShipAdmin(admin.ModelAdmin):
    pass


class SchoolClassMasterShipAdmin(admin.ModelAdmin):
    pass


class TeacherMessageAdmin(admin.ModelAdmin):
    pass


class TeacherScheduleAdmin(admin.ModelAdmin):
    pass


class SchoolClassAdmin(admin.ModelAdmin):
    pass


class SubjectsTemplateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherTermShip, TeacherTermShipAdmin)
admin.site.register(SchoolClassTeacherShip, SchoolClassTeacherShipAdmin)
admin.site.register(SchoolClassMasterShip, SchoolClassMasterShipAdmin)
admin.site.register(TeacherMessage, TeacherMessageAdmin)
admin.site.register(TeacherSchedule, TeacherScheduleAdmin)
admin.site.register(SchoolClass, SchoolClassAdmin)
admin.site.register(SubjectsTemplate, SubjectsTemplateAdmin)
