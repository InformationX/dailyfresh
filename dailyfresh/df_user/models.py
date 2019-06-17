from django.db import models

# Create your models here.
class UserInfo(models.Model):

    user_name = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.CharField(max_length=20, verbose_name='邮箱')
    phone = models.CharField(max_length=11, verbose_name='电话')
    recv_name = models.CharField(max_length=20, verbose_name='收件人')
    you_bian = models.CharField(max_length=6, verbose_name='邮政编码')
    address = models.CharField(max_length=100, verbose_name='收货地址')