# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.teacher.views import TeacherIndexView, ConnectParentsView, WriteToParentsView, TeacherClassesView, \
    TeacherClassDetailView, TeacherClassStudentsView
from applications.teacher.route.message import urlpatterns as message_url
from applications.teacher.route.term import urlpatterns as term_url
from applications.teacher.route.schedule import urlpatterns as schedule_url
from settings.const import URL_ID, CLASS_ID

urlpatterns = patterns('',
    url(r'^index/$', TeacherIndexView.as_view(), name='teacher_index_view'),
    url(r'^handle/evaluation/$', ConnectParentsView.as_view(), name='teacher_handle_evaluation_view'),
    url(r'^to/parent/$', WriteToParentsView.as_view(), name='teacher_write_to_parent_view'),
    url(r'^%s/classes/$' % URL_ID, TeacherClassesView.as_view(), name='teacher_classes_view'),
    url(r'^class/%s/detail/$' % URL_ID, TeacherClassDetailView.as_view(), name='teacher_class_detail_view'),
    url(r'^class/%s/students/$' % CLASS_ID, TeacherClassStudentsView.as_view(), name='teacher_class_students_view')
)

urlpatterns += message_url

urlpatterns += term_url

urlpatterns += schedule_url