from django.conf.urls import url
from goods import views
from django.urls import include, path

app_name = 'apps.goods'
urlpatterns = [
    url('test/', views.TestView.as_view(), name='test'),  # 测试页
    path('detail/<int:goods_id>', views.DetailView.as_view(), name='detail'),  # 详情页
    path('list/<int:types_id>/<int:page>', views.ListView.as_view(), name='list'),  # 详情页
    # path('active/<int:token>', views.ActiveView.as_view(), name='active'),  # 测试传参数 为啥只有设置 path才行并且前面不能加goods的空间域名？
    url('', views.IndexView.as_view(), name='index'),  # 首页
]

