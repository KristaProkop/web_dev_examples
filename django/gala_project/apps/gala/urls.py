from django.conf.urls import url
from django.contrib import admin
from . import views 

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^rsvp$', views.rsvp, name='rsvp'),
  url(r'^rsvp_user$', views.rsvp_user, name='rsvp_user'),
  url(r'^rsvp_detail$', views.rsvp_detail, name='rsvp_detail'),
  url(r'^reports$', views.reports, name='reports'),
  url(r'^hotel$', views.hotel, name='hotel'),
]