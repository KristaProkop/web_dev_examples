from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin$', views.login, name="login"),
    url(r'^logoff$', views.logoff, name="logoff"),
    url(r'^register$', views.register, name="register"),
    url(r'^update_user/(?P<id>\d+)/(?P<category>\d+)$', views.update_user, name="update_user"),
    url(r'^new_user$', views.create_user, name="create_user"),
    url(r'^delete/(?P<id>\d+)$', views.destroy, name="delete_user"),
]