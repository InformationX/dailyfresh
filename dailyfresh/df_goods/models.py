from DjangoUeditor.models import UEditorField
from django.db import models

# Create your models here.


class TypeInfo(models.Model):
    type_title = models.CharField('类型名称', max_length=20)
    is_delete = models.BooleanField('是否删除', default=False)

    def __str__(self):
        return self.type_title

    class Meta:
        verbose_name = '分类信息'
        verbose_name_plural = '分类信息'

class GoodsInfo(models.Model):
    goods_title = models.CharField('商品名称', max_length=20)
    goods_name = models.CharField('商品简称', max_length=20, null=True, blank=True)
    goods_pic = models.ImageField('商品图片', upload_to='df_goods', null=True, blank=True)  # 商品图片
    goods_price = models.DecimalField('商品价格', max_digits=7, decimal_places=2)  # 总共最多有7位,小数占2位
    goods_unit = models.CharField('商品单位', max_length=20, default='500g')  # 商品的单位
    goods_click = models.IntegerField('点击量')  # 商品点击量,便于排人气
    is_Delete = models.BooleanField('是否删除', default=False)
    goods_jianjie = models.CharField('简介', max_length=200)  # 商品简介
    goods_kucun = models.IntegerField('库存')  # 商品库存
    goods_content = UEditorField('详细介绍', height=300, width=1000)  # 商品详细内容
    goods_type = models.ForeignKey(TypeInfo, verbose_name='所属分类', on_delete=models.CASCADE)  # 商品所属类型


    # gadv = models.BooleanField(default=False)   #商品推荐
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'