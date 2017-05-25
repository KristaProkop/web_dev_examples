from django.conf.urls import url
from . import views
from .views import UserView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^generate_key$', views.generate_key, name='generate_key'),
    url(r'^create$', views.create_tweet, name='create_tweet'),
    url(r'^retrieve$', views.decrypt_tweet, name='decrypt_tweet'),
    url(r'^users/$', UserView.as_view()),
]