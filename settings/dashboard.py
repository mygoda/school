# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    title = u"赫兹租车管理系统"

    def init_with_context(self, context):
        site_name = u"赫兹租车"

        self.children.append(modules.ModelList(
            u"用户管理",
            column=1,
            collapsible=True,
            models=(
                'applications.users.models.User',
            )
        ))

        self.children.append(modules.ModelList(
            u"微信管理",
            column=1,
            collapsible=True,
            models=(
                'applications.weixin.models.apps.App',
                'applications.weixin.models.rules.Rule',
                'applications.weixin.models.photos.Photo',
                'applications.weixin.models.photos.RichText',
                'applications.weixin.models.token.WeixinUserToken',
            )
        ))

        self.children.append(modules.ModelList(
            u"消息管理",
            column=2,
            collapsible=True,
            models=(
                'applications.meeting.models.message.Message',
            )
        ))


        self.children.append(modules.ModelList(
            u"系统管理",
            column=2,
            collapsible=True,
            models=(
                'applications.base.models.ServerSetting',
                'applications.meeting.models.setting.SystemSetting',
                'applications.meeting.models.setting.CheckInSetting',
                'applications.meeting.models.setting.PrinterSetting'
            )
        ))

        self.children.append(modules.ModelList(
            u"服务监控",
            column=3,
            collapsible=True,
            models=(
                'applications.base.models.ErrorLog',
            )
        ))

