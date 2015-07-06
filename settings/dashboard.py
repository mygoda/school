# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    title = u"校园管理系统"

    def init_with_context(self, context):
        site_name = u"学校管理"

        self.children.append(modules.ModelList(
            u"用户管理",
            column=1,
            collapsible=True,
            models=(
                'applications.users.models.User',
                'applications.api.models.UserPassword',
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
            u"教师管理",
            column=1,
            collapsible=True,
            models=(
                'applications.teacher.models.teacher.Teacher',
                'applications.teacher.models.teacher.Term',
                'applications.teacher.models.teacher.SchoolClassTeacherShip',
                'applications.teacher.models.teacher.SchoolClassMasterShip',
                'applications.teacher.models.teacher.TeacherTermShip',
                'applications.teacher.models.schedule.TeacherSchedule',
                'applications.teacher.models.schoolClass.SchoolClass',
                'applications.teacher.models.subjects.SubjectsTemplate',
            )
        ))


        self.children.append(modules.ModelList(
            u"消息管理",
            column=2,
            collapsible=True,
            models=(
                'applications.teacher.models.message.TeacherMessage',
            )
        ))



        self.children.append(modules.ModelList(
            u"学生管理",
            column=2,
            collapsible=True,
            models=(
                'applications.students.models.students.Students',
                'applications.students.models.students.StudentGrade',
                'applications.students.models.students.StudentHomework',
            )
        ))


        self.children.append(modules.ModelList(
            u"统计管理",
            column=2,
            collapsible=True,
            models=(
                'applications.statistics.models.terms.TermStatistics',
            )
        ))