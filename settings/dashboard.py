# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

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
            u"会议管理",
            column=1,
            collapsible=True,
            models=(
                'applications.meeting.models.meeting.Meeting',
                'applications.meeting.models.meeting.Ticket',
                'applications.meeting.models.meeting.MeetingBank',
            )
        ))

        self.children.append(modules.ModelList(
            u"门票管理",
            column=2,
            collapsible=True,
            models=(
                'applications.meeting.models.meeting.Agent',
                'applications.meeting.models.meeting.TicketTemplate',
                'applications.meeting.models.meeting.AgentTicketShip',
                'applications.meeting.models.order.TicketCheckInHistory',
            )
        ))


        self.children.append(modules.ModelList(
            u"订单管理",
            column=1,
            collapsible=True,
            models=(
                'applications.meeting.models.order.ShoppingCart',
                'applications.meeting.models.order.Order',
                'applications.meeting.models.code.Code',
            )
        ))

        self.children.append(modules.ModelList(
            u"预约管理",
            column=1,
            collapsible=True,
            models=(
                'applications.meeting.models.schedule.Schedule',
                'applications.meeting.models.schedule.UserSchedule',
            )
        ))

        self.children.append(modules.ModelList(
            u"订单",
            column=2,
            collapsible=True,
            models=(
                'applications.order.models.Trade',
                'applications.meeting.models.order.Ticket',
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
            u"门票打印",
            column=2,
            collapsible=True,
            models=(
                'applications.meeting.models.meeting.PrintTemplate',
                'applications.meeting.models.meeting.MeetingTemplateShip',
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

        self.children.append(modules.ModelList(
            u"调查问卷",
            column=3,
            collapsible=True,
            models=(
                'applications.meeting.models.survey.MeetingSurvey',
                'applications.meeting.models.survey.ClassSurvey',
            )
        ))

        self.children.append(modules.ModelList(
            u"证书",
            column=3,
            collapsible=True,
            models=(
                'applications.meeting.models.certificate.Certificate',
                'applications.meeting.models.certificate.UserCertificate',
            )
        ))

        # self.children.append(modules.ModelList(
        #     u"微信订单信息",
        #     column=3,
        #     collapsible=True,
        #     models=(
        #         'applications.payment.models.WeChatPayment',
        #     )
        # ))
