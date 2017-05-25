from django.conf.urls import url
from django.contrib import admin
from . import views 

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^register$', views.register, name='register'),
  url(r'^login$', views.login, name='login'),
  url(r'^logout$', views.logout, name='logout'),
  url(r'^friends$', views.friends, name='friends'),
  url(r'^users/(?P<id>\d+)$', views.show_friend, name='show_friend'),
  url(r'^users/add/(?P<id>\d+)$', views.create_friend, name='create_friend'),
  url(r'^users/remove/(?P<id>\d+)$', views.destroy_friend, name="destroy_friend"),
]