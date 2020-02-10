from django.shortcuts import render, redirect
from user import models
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.conf import settings

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer #进行加密
import re
import time

# /user/register
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        #接受数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        #进行数据校验
        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg':'数据不完整'})
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})
        try:
            user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            user = None
        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})
        #创建用户
        user = models.User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        #返回页面
        return render(request, 'register.html', {'errmsg': '用户名注册成功'})

# /user/logout
class LogoutView(View):
    '''退出登录'''
    def get(self, request):
        #清除用户的session信息
        logout(request)
        return redirect(reverse('goods:index'))

# /user/login
class LoginView(View):
    '''登录页面'''
    def get(self, request):
        return render(request, 'login.html')

# /user/api
class ApiView(View):
    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        data = {}
        print(username, password)
        if not all([username, password]):
            data['code'] = 2
            data['msg'] = '数据不完整'
            return JsonResponse(data)
        user = authenticate(username=username, password=password)
        if user is not None:
            #用户名密码正确
            login(request, user)
            data['code'] = 1
            data['msg'] = '用户登录成功'
            return JsonResponse(data)
        else:
            data['code'] = 3
            data['msg'] = '用户名密码错误'
            return JsonResponse(data)


# /user/test
class TestView(View):
    def get(self, request):
        user = request.user
        print(user)
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})
        return HttpResponse('ahahahah')


