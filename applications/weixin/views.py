# -*- coding: utf-8 -*-
# __author__ = xutao

from __future__ import division, unicode_literals, print_function
from urllib import unquote_plus
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView
from applications.users.models import User
from applications.weixin.models import RichText
from applications.weixin.models.token import WeixinUserToken
from applications.weixin.weixin.receiver import WeiXinReceiver


class WeiXinResponseView(View):
    def get(self, request, *args, **kwargs):
        receiver = WeiXinReceiver(request)
        return HttpResponse(receiver.echo())

    def post(self, request, *args, **kwargs):
        receiver = WeiXinReceiver(request)
        return HttpResponse(receiver.dispatch())

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WeiXinResponseView, self).dispatch(request, *args, **kwargs)


class WeiXinDetailView(TemplateView):
    template_name = "text_detail.html"

    def get_context_data(self, **kwargs):
        rich_text = RichText.get_by_unique(**kwargs)
        if not rich_text:
            raise Http404("没有指定的图文消息")

        context = super(WeiXinDetailView, self).get_context_data(**kwargs)
        context['rich_text'] = rich_text
        return context


class WeixinOAuthRedirectView(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code", "")
        redirect_uri = unquote_plus(request.GET.get("redirect_uri", ""))
        state = request.GET.get("state", "")
        user = request.user
        self.fetch_access_token(request, user, code)
        return HttpResponseRedirect(redirect_uri)

    def fetch_access_token(self, request, user, code):
        # 逻辑
        # 1. 没登陆：如果曾经创建过会员，帮他登陆
        # 2. 如果没创建过，新建会员，帮他登陆
        # 3. 登陆了：如果没授权，授权之
        # 4. 登陆了：已有授权，不干什么

        # 可能出现的问题：没登陆，但是之前有会员且未授权，会出现重新授权的问题。

        json_data = WeixinUserToken.fetch_access_json(code)
        if not user.is_authenticated():
            token = WeixinUserToken.get_token_by_openid(json_data['openid'])
            if token:
                user = token.user
            else:
                user = User()
                user.save()

            user = authenticate(id=user.id)
            login(request, user)
        else:
            try:
                token = user.weixinusertoken
            except:
                pass
        token = WeixinUserToken.get_or_update_token(user, json_data)
        return token