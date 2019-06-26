from django.conf.urls import url

from df_carts import views

urlpatterns = [
    url('^cart/$', views.cart),
]