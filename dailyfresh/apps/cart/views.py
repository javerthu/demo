from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from goods.models import GoodsSKU
from django_redis import get_redis_connection
# from utils.mixin import LoginRequiredMixin

# Create your views here.
# 添加商品到购物车
# 1) 请求方式，采用ajax post
#    如果涉及到数据的修改(新增，更新，删除),采用post
#    如果涉及到数据的获取, 采用get
# 2) 传递参数：商品id 商品数量


# ajax发起的请求都在后台, 在浏览器中看不到效果
# /cart/add
class CartAddView(View):
    """购物车记录添加"""
    def post(self, request):

        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'}) #显示在弹网页弹出的对话框

        # 接收数据
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        # 数据校验
        if not all([sku_id, count]):
            return JsonResponse({'res': 1, 'errmsg': '数据不完整'})

        # 校验添加的商品数量
        # noinspection PyBroadException
        try:
            count = int(count)
        except Exception as e:
            return JsonResponse({'res': 2, 'errmsg': '商品数目出错'})

        # 校验商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '商品不存在'})

        # 业务处理：添加购物车记录
        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id
        # 先尝试获取sku_id的值 -> hget cart_key 属性: cart_key[sku_id]
        # 如果sku_id在hash中不存在，hget返回None
        cart_count = conn.hget(cart_key, sku_id)
        if cart_count:
            # redis中存在该商品，进行数量累加
            count += int(cart_count)

        # 校验商品的库存
        if count > sku.stock:
            return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})
        # 设置hash中sku_id对应的值
        # hset ->如sku_id存在,更新数据,如sku_id不存在，追加数据
        conn.hset(cart_key, sku_id, count)

        # 获取用户购物车中的条目数
        cart_count = conn.hlen(cart_key)

        # 返回应答
        return JsonResponse({'res': 5, 'cart_count': cart_count, 'message': '添加成功'})

# /cart/
class CartView(View):
    """购物车显示"""
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'}) #显示在弹网页弹出的对话框
        #查询redis数据库中用户购物车缓存的数据，主要是拿sku_id
        # 业务处理：添加购物车记录
        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id
        # {'商品id': 商品数量}
        cart_dict = conn.hgetall(cart_key)
        tol_count = 0
        tol_price = 0
        sku_list = []
        for i in cart_dict:
            sku = GoodsSKU.objects.get(id=i)
            count = int(cart_dict[i])
            tol_count = tol_count + count
            sku.count = count
            amount = count*sku.price
            tol_price = tol_price + amount
            sku.amount = amount
            sku_list.append(sku)
        length = len(sku_list)
        # for i in sku_list:
        #     print(i.name, i.count)

        context = {
            'sku_list': sku_list, 'length': length,
            'total_count': tol_count, 'total_price': tol_price,
        }

        return render(request, 'cart.html', context=context)


# 更新购物车记录
# 采用ajax post请求
# 前端需要传递的参数: 商品id(sku_id) 更新商品数量(count)
# /cart/update
class CartUpdateView(View):
    """购物车记录更新"""
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        # 接收数据
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        # 数据校验
        if not all([sku_id, count]):
            return JsonResponse({'res': 1, 'errmsg': '数据不完整'})

        # 校验添加的商品数量
        # noinspection PyBroadException
        try:
            count = int(count)
        except Exception as e:
            return JsonResponse({'res': 2, 'errmsg': '商品数目出错'})

        # 校验商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '商品不存在'})

        # 业务处理: 更新购物车记录
        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id

        # 校验商品的库存
        if count > sku.stock:
            return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})
        # 设置hash中sku_id对应的值,更新
        # hset ->如sku_id存在,更新数据,如sku_id不存在，追加数据
        conn.hset(cart_key, sku_id, count)

        # # 计算用户购物车中商品的总件数{'1':5,'2':3}
        # total_count = 0
        # vals = conn.hvals(cart_key)
        # for val in vals:
        #     total_count += int(val)

        # 返回应答
        return JsonResponse({'res': 5, 'message': '更新成功'})


# 删除购物车记录
# 采用ajax post请求
# 前端需要传递的参数: 商品id(sku_id)
# /cart/delete
class CartDeleteView(View):
    """购物车记录删除"""
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        # 接收参数
        sku_id = request.POST.get('sku_id')

        # 数据校验
        if not sku_id:
            return JsonResponse({'res': 1, 'errmsg': '无效的商品id'})

        # 校验商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res': 2, 'errmsg': '商品不存在'})

        # 业务处理: 删除购物车记录
        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id

        # 删除 hdel
        conn.hdel(cart_key, sku_id)

        # 计算用户购物车中商品的总件数{'1':5,'2':3}
        total_count = 0
        #hvals返回redis库中哈希的所有vaule
        vals = conn.hvals(cart_key)
        for val in vals:
            total_count += int(val)

        return JsonResponse({'res': 3, 'message': '删除成功'}) # 'total_count': total_count,
