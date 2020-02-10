from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.core.paginator import Paginator #django自带分页类
from goods import models
from order.models import OrderGoods
from django_redis import get_redis_connection

#/
class IndexView(View):

    def get(self, request):
        print(request.path,'主页')
        #获取商品种类信息
        types = models.GoodsType.objects.all()  #all() filter(logo='fruit')

        #获取首页轮播商品信息
        goods_banners = models.IndexGoodsBanner.objects.all().order_by('index')

        #获取首页分类商品展示信息
        for type in types:
            type_goods_banners = models.IndexTypeGoodsBanner.objects.filter(type=type)[0:4]
            #将查出的type_goods_banners动态添加给type
            type.show_obj = type_goods_banners
        # for i in types.show_obj:
        #     print(i.sku.name, i.sku.price, i.sku.image)

        #获取用户购物车中的商品数目
        user = request.user
        cart_count = 0
        if user.is_authenticated: ##user.is_authenticated不要加括号！！
            #用户登录了
            conn = get_redis_connection('default')
            cart_key = 'cart_%d'%user.id
            cart_count = conn.hlen(cart_key)  #有多少条目数

        #组织模板上下文
        context = {
            'types': types,
            'goods_banners': goods_banners,
            # 'promotion_banners': promotion_banners,
            'cart_count': cart_count,
        }


        return render(request, 'index.html', context=context)


from rest_framework.views import APIView #APIView是View的子类
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from utils import serilaz
import json

#自定义分页功能
class MyPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'size' #还可以在url加一个size参数选择显示多少个
    max_page_size = 15 #即使加了size参数最大显示15条

    page_query_param = 'page' #翻页的参数
class ApiView(APIView):

    def get(self, request):
        print('11111')
        # types = models.GoodsType.objects.get_queryset().order_by('id')
        # ser_types = serilaz.ser_GoodsType(instance=types, many=True)
        #
        # goods_banners = models.IndexGoodsBanner.objects.get_queryset().order_by('id')
        # ser_goods_banners = serilaz.ser_IndexGoodsBanner(instance=goods_banners, many=True)

        #获取首页促销活动信息
        promotion_banners = models.IndexPromotionBanner.objects.get_queryset().order_by('-index')
        ser_promotion_banners = serilaz.ser_IndexPromotionBanner(instance=promotion_banners, many=True)
        x = {
            # 'ser_types':ser_types.data,
            # 'ser_goods_banners':ser_goods_banners.data,
            'ser_promotion_banners': ser_promotion_banners.data,
        }
        return Response(x)

class TestApiView(APIView):

    def get(self, request):
        print('11111')
        types = models.GoodsType.objects.all().order_by('id')[0:4]
        ser_types = serilaz.ser_GoodsType(instance=types, many=True)
        #
        # goods_banners = models.IndexGoodsBanner.objects.get_queryset().order_by('id')
        # ser_goods_banners = serilaz.ser_IndexGoodsBanner(instance=goods_banners, many=True)

        #获取首页促销活动信息
        # promotion_banners = models.IndexPromotionBanner.objects.get_queryset().order_by('-index')
        # ser_promotion_banners = serilaz.ser_IndexPromotionBanner(instance=promotion_banners, many=True)
        x = {
            'ser_types':ser_types.data,
            # 'ser_goods_banners':ser_goods_banners.data,
            # 'ser_promotion_banners': ser_promotion_banners.data,
        }
        return Response(x)

# /detail/id   商品详情页
class DetailView(APIView):
    def get(self, request, goods_id):
        # # 获取商品sku详细信息
        # try:
        #     goods_sku = models.GoodsSKU.objects.filter(id=goods_id)[0] #filter(id=goods_id)[0] , get(id=goods_id)
        # except:  #商品不存在
        #     return redirect(reverse('goods:index'))
        #
        #
        # # 获取商品的评论信息
        # sku_orders = OrderGoods.objects.filter(sku=goods_sku).exclude(comment='')
        #
        # #获取新品推荐信息
        # try:
        #     new_skus = models.GoodsSKU.objects.filter(type=goods_sku.type).order_by('-create_time').exclude(id=goods_id)[0:2]
        # except:
        #     new_skus = None

        # 获取用户购物车中的商品数目
        user = request.user
        cart_count = 0
        if user.is_authenticated:  ##user.is_authenticated不要加括号！！
            # 用户登录了
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)

            #添加历史浏览记录
            conn = get_redis_connection('default')
            history_key = 'history_%d'%user.id
            #移除表中的goods_id
            conn.lrem(history_key, 0, goods_id)
            #把good_id插入到表的左侧
            conn.lpush(history_key, goods_id)
            #只保存用户最新浏览的5条信息
            conn.ltrim(history_key, 0, 4)
        # for i in sku_orders:
        #     print(i.comment, i.order.user.username, str(i.update_time)[0:10])

        # 组织模板上下文
        context = {
            # 'goods_sku': goods_sku,
            # 'sku_orders': sku_orders,
            # 'new_skus': new_skus,
            'cart_count': cart_count,
        }

        return render(request, 'detail.html', context=context)

    def post(self, request, goods_id):
        x = {}

        # 获取商品sku详细信息
        try:
            x['code'] = 1
            types = models.GoodsType.objects.all().order_by('id')
            ser_types = serilaz.ser_GoodsType(instance=types, many=True)
            x['ser_types'] = ser_types.data
            goods_sku = models.GoodsSKU.objects.get(id=goods_id) #filter(id=goods_id)[0] , get(id=goods_id)
            ser_sku = serilaz.ser_GoodsSKU(instance=goods_sku, many=False)
            x['ser_sku'] = ser_sku.data
            x['msg'] = '查询成功'
        except:  #商品不存在
            x['code'] = 0
            x['msg'] = '商品不存在'
            return Response(x)


        # 获取商品的评论信息
        sku_orders = OrderGoods.objects.filter(sku=goods_sku).exclude(comment='')

        #获取新品推荐信息
        try:
            new_skus = models.GoodsSKU.objects.filter(type=goods_sku.type).order_by('-create_time').exclude(id=goods_id)[0:2]
        except:
            new_skus = None

        print(111111111111111,'detail')
        print(goods_id)
        print(x)
        return Response(x)



