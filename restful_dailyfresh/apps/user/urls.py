from django.conf.urls import url
from user import views
from django.urls import path

app_name = 'apps.user'
urlpatterns = [
    url('register', views.RegisterView.as_view(), name='register'),  # 注册页面 CBV
    url('login', views.LoginView.as_view(), name='login'),  # 登录页面
    url('logout/', views.LogoutView.as_view(), name='logout'),  # 退出登录连接
    path('test', views.TestView.as_view(), name='test'),  # 查询测试 ajax
    path('api', views.ApiView.as_view(), name='api'),  # 查询测试 ajax
]

