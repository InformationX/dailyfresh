from django.shortcuts import render

# Create your views here.
from df_goods.models import *


def index(request):             #主页
    typelist = TypeInfo.objects.all()  # 首先获得外键指向的表中对象，然后通过‘_set’这样的方法获得目标表中的数据
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]  # 按降序获得,获得最大的
    type01 = typelist[0].goodsinfo_set.order_by('-goods_click')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-goods_click')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-goods_click')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-goods_click')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-goods_click')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-goods_click')[0:4]
    context = {
        'title': '首页',
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }
    return render(request, 'df_goods/index.html', context)
