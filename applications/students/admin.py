# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.contrib import admin
from applications.students.models.students import StudentGrade, Students, StudentHomework


class StudentsAdmin(admin.ModelAdmin):
    pass


class StudentsGradeAdmin(admin.ModelAdmin):
    pass


class StudentHomeworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Students, StudentsAdmin)
admin.site.register(StudentGrade, StudentsGradeAdmin)
admin.site.register(StudentHomework, StudentHomeworkAdmin)