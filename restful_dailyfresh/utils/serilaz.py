from rest_framework import serializers
from goods import models

class ser_GoodsSKU(serializers.ModelSerializer):
    class Meta:
        model = models.GoodsSKU
        exclude = ['create_time', 'update_time', 'is_delete', ]

class ser_GoodsType(serializers.ModelSerializer):
    class Meta:
        model = models.GoodsType
        exclude = ['create_time', 'update_time', 'is_delete', ]
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

