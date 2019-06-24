from django.contrib import admin
from . models import *

# Register your models here.

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_title']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ['id', 'goods_title', 'goods_price', 'goods_unit','goods_click', 'goods_kucun', 'goods_content', 'goods_type']

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)