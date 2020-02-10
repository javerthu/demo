from rest_framework import serializers
from order.models import OrderGoods
from goods import models


class ser_OrderGoods(serializers.ModelSerializer):
    comment_user = serializers.CharField(source='order.user.username') #自定义一个字段就不用采用深度了
    class Meta:
        model = OrderGoods
        fields = ['update_time', 'comment', 'comment_user']

class ser_GoodsSKU(serializers.ModelSerializer):
    sku_type = serializers.CharField(source='type.name') #自定义一个字段就不用采用深度了
    sku_detail = serializers.CharField(source='goods.detail')
    class Meta:
        model = models.GoodsSKU
        fields = ['name', 'desc', 'price', 'unite', 'image', 'sku_type', 'sku_detail', 'id']

class ser_GoodsType(serializers.ModelSerializer):
    class Meta:
        model = models.GoodsType
        exclude = ['create_time', 'update_time', 'is_delete', 'id']
        # fields = '__all__'
        # ordering = ['id']

class ser_IndexGoodsBanner(serializers.ModelSerializer):
    class Meta:
        model = models.IndexGoodsBanner
        exclude = ['create_time', 'update_time', 'is_delete', ]

class ser_IndexPromotionBanner(serializers.ModelSerializer):
    class Meta:
        model = models.IndexPromotionBanner
        exclude = ['create_time', 'update_time', 'is_delete', ]

