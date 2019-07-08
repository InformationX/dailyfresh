from django.db import models

# Create your models here.


class OrderInfo(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey('df_user.UserInfo')
    order_date = models.DateTimeField(auto_now=True)
    order_IsPay = models.BooleanField(default=False)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_address = models.CharField(max_length=150, null=True, blank=True)

class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo')
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()
