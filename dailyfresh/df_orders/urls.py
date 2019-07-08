from django.conf.urls import url

from df_orders import views

urlpatterns = [
   url('^order/$', views.order),
]