from django.contrib import admin

from .models import GoodsType, GoodsSKU

# Register your models here.

class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

class GoodsSKUAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'desc', 'price', 'unite', 'stock', 'sales', 'status']

admin.site.register(GoodsSKU, GoodsSKUAdmin)
admin.site.register(GoodsType, GoodsTypeAdmin)
