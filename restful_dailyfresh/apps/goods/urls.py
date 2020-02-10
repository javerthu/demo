from django.conf.urls import url
from goods import views
from django.urls import include, path

app_name = 'apps.goods'
urlpatterns = [
    url('api/test', views.TestApiView.as_view(), name='test'),  # test
    url('api/', views.ApiView.as_view(), name='api'),  # api
    path('detail/<int:goods_id>', views.DetailView.as_view(), name='detail'),  # 详情页
    url('', views.IndexView.as_view(), name='index'),  # 首页
]

