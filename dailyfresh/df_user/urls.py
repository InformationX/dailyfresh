from django.conf.urls import url

from df_user import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_exist/$',views.register_exist),
    url(r'^login/$', views.login),
]
