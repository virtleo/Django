from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
import re

class AdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        #print("middleware_init_")

    def __call__(self, request):
        #print("middleware_call_"+request.path)
        path = request.path #获取本次请求的路径
        #print("请求路径：",path)
        #判断当前请求是否是以diancan开始
        if re.match('^/diancan/',path):
            # 检测session中是否存在 diancan_user 的数据记录
            if request.session.get('diancan_user','') == '':
                # 如果在session没有记录,则证明没有登录,跳转到登录页面
                return redirect(reverse('login'))

        #放行，继续往下走
        response = self.get_response(request)
        return response