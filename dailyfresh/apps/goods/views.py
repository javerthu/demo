from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.core.paginator import Paginator #django自带分页类
from goods import models
from django_redis import get_redis_connection
# Create your views here.
#/goods/test/
class TestView(View):
    def get(self, request):
        # goods_sku = models.GoodsSKU.objects.filter(type_id=2).order_by('id')
        # goods_sku = ['john', 'paul', 'george', 'ringo']
        # 对数据进行分页
        # paginator = Paginator(goods_sku, 1)  # 传入的goods_sku QuerySet要排序不然会报错  ,.object_list可以取其中每页的QuerySet
        # try:
        #     page = int(4)
        # except Exception as e:
        #     page = 1
        #
        # if page > paginator.num_pages or page <= 0:
        #     page = 1

        # 获取第page页的Page实例对象
        # page = 3
        # skus_page = paginator.page(page)
        # for pageindex in skus_page.paginator.page_range:
        #     print(pageindex)
        # print(goods_sku)
        # print(skus_page.paginator.page_range, skus_page.next_page_number(), skus_page.object_list)
        return render(request, 'user_center_info.html')

#/
class IndexView(View):

    def get(self, request):
        print(request.path,'主页')
        #获取商品种类信息
        types = models.GoodsType.objects.all()  #all() filter(logo='fruit')

        #获取首页轮播商品信息
        goods_banners = models.IndexGoodsBanner.objects.all().order_by('index')

        #获取首页促销活动信息
        promotion_banners = models.IndexPromotionBanner.objects.all().order_by('index')

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
            'promotion_banners': promotion_banners,
            'cart_count': cart_count,
        }


        return render(request, 'index.html', context=context)

# /active/token 测试传参数
# class ActiveView(View):
#     '''用户激活'''
#     def get(self, request, token):
#         print(token)
#         #解密加密的token
#         return render(request, 'register.html')


# /detail/id   商品详情页
class DetailView(View):
    def get(self, request, goods_id):
        # 获取商品sku详细信息
        try:
            goods_sku = models.GoodsSKU.objects.filter(id=goods_id)[0] #filter(id=goods_id)[0] , get(id=goods_id)
        except:  #商品不存在
            return redirect(reverse('goods:index'))

        # 获取商品种类信息
        types = models.GoodsType.objects.all()  # all() filter(logo='fruit')

        #获取新品推荐信息
        try:
            new_skus = models.GoodsSKU.objects.filter(type=goods_sku.type).order_by('-create_time').exclude(id=goods_id)[0:2]
        except:
            new_skus = None
        #获取同中商品不同规格的SPU
        # try:
        #     same_new_skus = models.GoodsSKU.objects.filter(goods=goods_sku.goods).order_by('-create_time').exclude(id=goods_id)
        # except:
        #     same_new_skus = None
        # print(same_new_skus)

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

        # 组织模板上下文
        context = {
            'types': types, #types,
            'goods_sku': goods_sku,
            'new_skus': new_skus,
            # 'same_new_skus': same_new_skus,
            'cart_count': cart_count,
        }

        return render(request, 'detail.html', context=context)

#商品列表 # /list/商品种类id/页面号码page
class ListView(View):

    def get(self, request, types_id, page):
        sort = request.GET.get('sort', 'default')
        if sort == 'price':
            sort = 'price'
        elif sort == 'hot':
            sort = 'sales'
        else:
            sort = 'id'
        # 获取商品sku详细信息
        try:
            goods_sku = models.GoodsSKU.objects.filter(type_id=types_id).order_by(sort)  #查询的所有对应的商品信息
        except:  #商品不存在
            return redirect(reverse('goods:index'))

        # 获取商品种类信息
        types = models.GoodsType.objects.all()  # all() filter(logo='fruit')
        goods_type = models.GoodsType.objects.get(id=types_id)  # 查询的对应的商品类型

        #获取新品推荐信息
        try:
            new_skus = models.GoodsSKU.objects.filter(type_id=types_id).order_by('-create_time')[0:2]
        except:
            new_skus = None

        #对数据进行分页   #skus_page.next_page_number() 没有下一页会报错！！md
        paginator = Paginator(goods_sku, 4)  #传入的goods_sku QuerySet要排序不然会报错  ,.object_list可以取其中每页的QuerySet对象
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages or page <= 0:
            page = 1

        # 获取第page页的Page实例对象
        skus_page = paginator.page(page)

        # # 进行页码的控制，页面上最多显示5个页码
        # # 1. 总数不足5页，显示全部
        # # 2. 如当前页是前3页，显示1-5页
        # # 3. 如当前页是后3页，显示后5页
        # # 4. 其他情况，显示当前页的前2页，当前页，当前页的后2页
        # num_pages = paginator.num_pages
        # if num_pages < 5:
        #     pages = range(1, num_pages)
        # elif page <= 3:
        #     pages = range(1, 6)
        # elif num_pages - page <= 2:
        #     pages = range(num_pages-4, num_pages+1)
        # else:
        #     pages = range(page-2, page+3)

        # 获取用户购物车中的商品数目
        user = request.user
        cart_count = 0
        if user.is_authenticated:  ##user.is_authenticated不要加括号！！
            # 用户登录了
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)

        context = {
            'types': types, 'goods_type': goods_type,
            'new_skus': new_skus,
            'goods_sku': goods_sku,
            'skus_page': skus_page,
            'cart_count': cart_count,
            'sort': sort,
        }

        return render(request, 'list.html', context=context)

