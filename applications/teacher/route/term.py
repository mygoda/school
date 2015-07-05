# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.teacher.controllers.term import TeacherCreateTermView, TeacherTermsView, TeacherTermDetailView, GetRecordStudentsGradeView, \
    HandleStudentsGradeView, TeacherCreateTermSuccessView, RecordGradeSuccessView, TermFilterByTypeView
from settings.const import TEACHER_ID, URL_ID

urlpatterns = patterns('',
    url(r'^create/term/$', TeacherCreateTermView.as_view(), name='teacher_create_view'),
    url(r'^create/term/success/$', TeacherCreateTermSuccessView.as_view(), name='teacher_create_term_success'),
    url(r'^%s/terms/$' % URL_ID, TeacherTermsView.as_view(), name='teacher_terms_view'),
    url(r'^term/%s/$' % URL_ID, TeacherTermDetailView.as_view(), name='teacher_term_detail_view'),
    url(r'^record/grade/$', GetRecordStudentsGradeView.as_view(), name='record_students_grade_view'),
    url(r'^record/grade/success/$', RecordGradeSuccessView.as_view(), name='record_student_grade_success_view'),
    url(r'term/detail/$', TeacherTermDetailView.as_view(), name='get_term_detail_view'),
    url(r'^handle/grade/$', HandleStudentsGradeView.as_view(), name='handle_record_students_grade_view'),
    url(r'^class/%s/term/filter/' % URL_ID, TermFilterByTypeView.as_view(), name='class_term_filter_view'),
)