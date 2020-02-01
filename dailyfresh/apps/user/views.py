# -*-coding:utf-8-*-
from django.shortcuts import render, redirect
from user import models
from order.models import OrderInfo, OrderGoods
from goods.models import GoodsSKU
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from django_redis import get_redis_connection

# from celery_tasks.tasks import send_register_active_email
from django.core.paginator import Paginator #django自带分页类
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer #进行加密
from itsdangerous import SignatureExpired
from utils.mixin import LoginRequiredMixin
import re
import time


# /user/register
# def register(request):
#     """注册"""
#     if request.method == "GET":
#         return render(request, 'register.html')
#
#     if request.method == "POST":
#         #接受数据
#         username = request.POST.get('user_name')
#         password = request.POST.get('pwd')
#         email = request.POST.get('email')
#         allow = request.POST.get('allow')
#         print(username, password, email, allow)
#
#         #进行数据校验
#         # 检验数据是否完整
#         if not all([username, password, email]):
#             return render(request, 'register.html', {'errmsg':'数据不完整'})
#         # 检验邮箱
#         if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
#             return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
#         # 检验是否同意协议
#         if allow != 'on':
#             return render(request, 'register.html', {'errmsg': '请同意协议'})
#         # 检验用户名是否存在
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             user = None
#         if user:
#             return render(request, 'register.html', {'errmsg': '用户名已存在'})
#
#         #进行业务注册
#         user = User.objects.create_user(username, email, password)
#
#         #返回应答,跳转到首页
#         return redirect(reverse('goods:index'))

# def register_handle(request):
#     """进行注册处理"""
#     if request.method == "POST":
#         #接受数据
#         username = request.POST.get('user_name')
#         password = request.POST.get('pwd')
#         email = request.POST.get('email')
#         allow = request.POST.get('allow')
#         print(username, password, email, allow)
#
#         #进行数据校验
#         # 检验数据是否完整
#         if not all([username, password, email]):
#             return render(request, 'register.html', {'errmsg':'数据不完整'})
#         # 检验邮箱
#         if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
#             return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
#         # 检验是否同意协议
#         if allow != 'on':
#             return render(request, 'register.html', {'errmsg': '请同意协议'})
#         # 检验用户名是否存在
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             user = None
#         if user:
#             return render(request, 'register.html', {'errmsg': '用户名已存在'})
#
#         #进行业务注册
#         user = User.objects.create_user(username, email, password)
#
#         #返回应答,跳转到首页
#         return redirect(reverse('goods:index'))
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
        #发送激活邮件，包含激活连接 /user/active/token
        #生成加密信息token
        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm':user.id}
        token = serializer.dumps(info) #注意是dumps不是dump
        token = token.decode('utf-8') #加密信息token是字节 解码后去除前面的b'
        #发邮件
        subject = '天天生鲜欢迎信息'
        message = ''
        html_message = '<h1>{},欢迎成为天天生鲜用户</h1>请点击下面连接激活您的账号</br>' \
                  '<a href="http://127.0.0.1:8000/user/active/{}">http://127.0.0.1:8000/user/active/{}</a>'.format(username, token, token)
        sender = settings.EMAIL_FROM
        receiver = [email]
        #发送
        send_mail(subject, message, sender, receiver, html_message=html_message)
        #返回页面
        return redirect(reverse('goods:index'))

# /user/active/token
class ActiveView(View):
    '''用户激活'''
    def get(self, request, token):
        #解密加密的token
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            user_id = info['confirm'] #待激活用户ID
            #激活用户
            user = models.User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            #返回应答，登录页面
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            return HttpResponse('激活连接已经过期')

# /user/login
class LoginView(View):
    '''登录页面'''
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        #接受数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        #验证数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})
        #业务处理:登录验证
        user = authenticate(username=username, password=password)
        if user is not None:
            #用户名密码正确
            if user.is_active:
                #用户已经激活
                #记录登录状态
                login(request, user)

                #获取登录后要跳转的地址
                next_url = request.GET.get('next', reverse('goods:index'))#默认返回首页url,跳转到登录页面的才有next参数的url
                return redirect(next_url)

                #跳转到首页
                # return redirect(reverse('goods:index'))
            else:
                # 去setting看，不设置user.is_active的else语句永远不会执行
                return render(request, 'login.html', {'errmsg': '用户未激活'})
        else:
            return render(request, 'login.html', {'errmsg': '用户名密码错误'})

# /user/logout
class LogoutView(View):
    '''退出登录'''
    def get(self, request):
        #清除用户的session信息
        logout(request)
        return redirect(reverse('goods:index'))

#/user
class UserInfoView(LoginRequiredMixin, View):
    '''用户中心-信息页'''
    def get(self, request):
        #page给模板传递一个是否点亮那栏的变量
        #request.user.is_authenticate()为TURE则表示登录
        #除了你给模板文件传递的模板变量外，django框架会把request.user也传递个模板变量
        user = request.user
        #获取用户个人基本信息
        try:
            user_info = models.Address.objects.filter(user=user)[0]
        except:
            user_info = None

        #获取用户的历史浏览记录
        conn = get_redis_connection('default')
        history_key = 'history_%d' % user.id
        watch_id = conn.lrange(history_key, 0, 4)  #redis中list值获取方法
        # print(watch_id)
        watch_info = []
        for id in watch_id:
            goods = GoodsSKU.objects.get(id=id)
            watch_info.append(goods)
        # print(watch_info)

        # print(watch_id)
        # watch_info = GoodsSKU.objects.filter(id__in=watch_id)  #这个不行，查出来的顺序不是按列表顺序排序的，而是按id顺序，查了半天没有解决
        # print(watch_info[0], watch_info)
        # ls = GoodsSKU.objects.filter(id=watch_id[0])
        # print(ls)

        context = {
            'user_info': user_info,
            'page': 'user',
            'watch_info': watch_info
        }
        return render(request, 'user_center_info.html', context=context)

#/user/order/page
class UserOrderView(LoginRequiredMixin, View):
    '''用户中心-订单页'''
    def get(self, request, page):
        #获取用户的订单信息
        user = request.user
        orders = OrderInfo.objects.filter(user=user).order_by('-create_time')

        #便利orders获取订单商品信息
        for order in orders:
            #根据order_id查询商品信息
            order_skus = OrderGoods.objects.filter(order_id=order.order_id)

            #遍历order_skus计算商品小计
            for order_sku in order_skus:
                #计算小计
                amount = order_sku.count*order_sku.price
                #动态给order_sku增加amount属性,保存订单商品的小计
                order_sku.amount = amount

            # 动态给order增加属性，保存商品状态信息
            order.status_name = OrderInfo.ORDER_STATUS[order.order_status]
            #动态给order增加属性，保存商品的信息
            order.order_skus = order_skus

        #分页
        # 对数据进行分页   #skus_page.next_page_number() 没有下一页会报错！！md
        paginator = Paginator(orders, 1)  # 传入的goods_sku QuerySet要排序不然会报错  ,.object_list可以取其中每页的QuerySet对象
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages or page <= 0:
            page = 1

        # 获取第page页的Page实例对象
        order_page = paginator.page(page)

        # 进行页码的控制，页面上最多显示5个页码
        # 1. 总数不足5页，显示全部
        # 2. 如当前页是前3页，显示1-5页
        # 3. 如当前页是后3页，显示后5页
        # 4. 其他情况，显示当前页的前2页，当前页，当前页的后2页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        #组织上下文模板变量
        context = {
            'order_page': order_page,
            'pages': pages,
            'page': 'order',
        }

        return render(request, 'user_center_order.html', context=context)

#/user/address
class AddressView(LoginRequiredMixin, View):
    '''用户中心-地址页'''
    def get(self, request):
        #获取用户的默认收货地址
        user = request.user
        try:
            # 获取用户的全部地址
            addrs = models.Address.objects.filter(user=user)
            address = models.Address.objects.get(user=user, is_default=True)
        except models.Address.DoesNotExist:
            address = None
        return render(request, 'user_center_site.html', {'page':'address', 'addrs': addrs, 'address':address})

    def post(self, request):
        #接受数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        #数据校验
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'page':'address', 'errmsg':'数据不完整'})

        # 校验邮编（看是否为六位数字）
        if zip_code and len(zip_code) != 6:
            return render(request, 'user_center_site.html', {'page': 'address', 'errmsg': '邮编错误'})

        # 校验手机号
        if not re.match(r'^1([3-8][0-9]|5[189]|8[6789])[0-9]{8}$', phone):
            return render(request, 'user_center_site.html', {'page':'address', 'errmsg':'手机号不正确'})

        #业务处理：添加收货地址
        #如果用户已经存在默认收货地址，添加的则不为默认收货地址
        user = request.user
        try:
            address = models.Address.objects.get(user=user, is_default=True)
        except models.Address.DoesNotExist:
            address = None

        if address:
            is_default = False
        else:
            is_default = True
        #添加地址库
        models.Address.objects.create(user=user, receiver=receiver,
                               addr=addr, zip_code=zip_code,
                               phone=phone, is_default=is_default)

        #返回应答,刷新地址页面
        return redirect(reverse('user:address')) #get请求在访问一次


