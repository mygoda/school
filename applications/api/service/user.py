# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from applications.api.service.base import ServiceBase
from applications.users.models import User


class UserModelSearchService(ServiceBase):
    model = User

    queryset_name = "users"

    obj_name = "user"


    search_fields = ['username__icontains', 'phone__icontains', "student_no__icontains"]

    page_size = 10

    def obj_to_json(self, obj):
        return {
            "id": obj.id,
            "username": obj.username,
            "phone": obj.hidden_phone,
        }