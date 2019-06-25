from django.core.paginator import Paginator
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

def list(request, tid, pindex, sort):
    """
    商品列表页
    :param request:
    :param tid: 所属分类
    :param pindex:分页
    :param sort: 排序方式
    :return:
    """
    typeinfo = TypeInfo.objects.get(id=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(tid)).order_by('-id')
    elif sort == '2':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(tid)).order_by('-goods_price')
    elif sort == '3':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(tid)).order_by('goods_click')
    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(pindex))
    context = {
        'title':typeinfo.type_title,
        'page':page,
        'typeinfo':typeinfo,
        'news':news,
        'sort':sort,
        'paginator':paginator,
    }
    return render(request, 'df_goods/list.html', context)


def detail(request, id):
    goods_id = GoodsInfo.objects.get(id=int(id))
    goods_id.goods_click = goods_id.goods_click + 1
    goods_id.save()
    goods_title = goods_id.goods_title
    goods_pic = goods_id.goods_pic
    goods_price = goods_id.goods_price
    goods_jianjie = goods_id.goods_jianjie
    goods_content = goods_id.goods_content
    goods_unit = goods_id.goods_unit
    news = goods_id.goods_type.goodsinfo_set.order_by('-id')[0:2]


    # goods_click
    context = {
        'goods_id':goods_id,
        'goods_title':goods_title,
        'goods_pic':goods_pic,
        'goods_price':goods_price,
        'goods_jianjie':goods_jianjie,
        'goods_content':goods_content,
        'goods_unit':goods_unit,
        'news':news,
    }
    return render(request, 'df_goods/detail.html', context)