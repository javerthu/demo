from django.conf.urls import url
from order import views as h
from django.urls import include, path

app_name = 'apps.order'

urlpatterns = [
    url('place', h.OrderPlaceView.as_view(), name='place'),  # 购物车更新页面
    url('commit', h.OrderCommitView.as_view(), name='commit'),  # 订单创建 悲观锁,乐观锁
    url('pay', h.OrderPayView.as_view(), name='pay'),  # 订单支付
    url('check', h.CheckPayView.as_view(), name='ckeck'),  # 查询支付交易结果
    # path('order/<int:page>', views.UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    path('comment/<order_id>', h.OrderCommentView.as_view(), name='comment'),  # 订单评论
]

