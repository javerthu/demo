from django.conf.urls import url
from django.urls import path
from user import views
from django.contrib.auth.decorators import login_required #进行登录验证django自带的user才可行，在本案例中就是重写了django的user表

app_name = 'apps.user'
urlpatterns = [
    # url('register/', views.register, name='register'),   # 注册页面 FBV
    url('register', views.RegisterView.as_view(), name='register'),# 注册页面 CBV
    # url('register_handle/', views.register_handle, name='register_handle'),#注册处理
    path('active/<token>', views.ActiveView.as_view(), name='active'),  # 激活地址
    url('login', views.LoginView.as_view(), name='login'),  # 登录页面
    url('logout/', views.LogoutView.as_view(), name='logout'),  # 退出登录连接

    # url('order/', login_required(views.UserOrderView.as_view()), name='order'),  # 用户中心-订单页
    # url('address/', login_required(views.AddressView.as_view()), name='address'),  # 用户中心-地址页
    # url('', login_required(views.UserInfoView.as_view()), name='user'),  # 用户中心-信息页  ''记得放到最后匹配，否则出错

    #在utils的mixin中做了视图的验证封装，只需要在需要登录验证的views函数中继承mixin中的LoginRequiredMixin类就行要放在左边
    # path('list/<int:types_id>/<int:page>', views.ListView.as_view(), name='list'),  # 详情页
    path('order/<int:page>', views.UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    url('address', views.AddressView.as_view(), name='address'),  # 用户中心-地址页
    url('', views.UserInfoView.as_view(), name='user'),  # 用户中心-信息页  ''记得放到最后匹配，否则出错
]

