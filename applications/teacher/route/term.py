# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from applications.teacher.controllers.term import TeacherCreateTermView, TeacherTermsView, TeacherTermDetailView
from settings.const import TEACHER_ID, URL_ID

urlpatterns = patterns('',
    url(r'^create/term/$', TeacherCreateTermView.as_view(), name='teacher_create_view'),
    url(r'^terms/$' % TEACHER_ID, TeacherTermsView.as_view(), name='teacher_terms_view'),
    url(r'^term/%s/$' % URL_ID, TeacherTermDetailView.as_view(), name='teacher_term_detail_view'),
)