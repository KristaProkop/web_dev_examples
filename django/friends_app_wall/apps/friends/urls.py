from django.conf.urls import url

from . import views 


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^friends/$', views.friends, name='friends'),
    url(r'^users/(?P<id>\d+)$', views.show_user, name='show_user'),
    url(r'^users/add/(?P<id>\d+)$', views.create_friendship, name='create_friendship'),
    url(r'^users/remove/(?P<id>\d+)$', views.destroy_friendship, name="destroy_friendship"),

    #Work in progress:
    # url(r'^users/edit/(?P<id>\d+)$', views.edit_profile, name='edit_profile'),
    # url(r'^users/edit/(?P<id>\d+)/images$', views.edit_profile_image, name='edit_profile_image'),
]
