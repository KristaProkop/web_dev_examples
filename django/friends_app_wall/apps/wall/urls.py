from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<friend_id>\d+)$', views.user_wall, name='user_wall'),
    url(r'^message/submit/(?P<wall_id>\d+)$', views.message_submit, name="message_submit"),
    url(r'^message/delete/(?P<message_id>\d+)$', views.message_delete, name='message_delete'),
    url(r'^comment/submit/(?P<message_id>\d+)$', views.comment_submit, name="comment_submit"),
    url(r'^comment/delete/(?P<comment_id>\d+)$', views.comment_delete, name='comment_delete'),
]