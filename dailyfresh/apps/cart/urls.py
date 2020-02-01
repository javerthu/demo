from django.conf.urls import url
from django.conf.urls import url
from cart import views as h

app_name = 'apps.cart'
urlpatterns = [
    url('add', h.CartAddView.as_view(), name='add'),  # 购物车页面
    url('update', h.CartUpdateView.as_view(), name='update'),  # 购物车更新页面
    url('delete', h.CartDeleteView.as_view(), name='delete'),  # 购物车删除地址
    url('', h.CartView.as_view(), name='cart'),  # 购物车页面
    # url(r'^delete$', h.CartDeleteView.as_view(), name='delete'),  # 删除购物车中的商品记录
]

