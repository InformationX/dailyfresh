from django.conf.urls import url

from df_carts import views

urlpatterns = [
    url('^$', views.cart),
    url(r'^add(\d+)_(\d+)/$', views.add),
    url(r'edit(\d+)_(\d+)/$', views.edit),
]