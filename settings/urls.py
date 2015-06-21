# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from applications.meeting.controllers.meeting import MeetingListTemplateView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^meetings/', include('applications.meeting.urls')),
    url(r'^api/', include('applications.api.urls')),
    url(r'^core/', include('applications.base.urls')),
    url(r'^weixin/', include('applications.weixin.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^editor/', include("applications.ueditor.urls")),
    url(r'^trades/', include("applications.order.urls")),
    url(r'^users/', include("applications.users.urls")),
    url(r'^backend/', include("applications.backend.urls")),
    url(r'^$', MeetingListTemplateView.as_view(), name=u"meeting_index_view"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    #(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes': True}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)