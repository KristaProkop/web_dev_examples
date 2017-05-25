from django.conf.urls import url, include
from django.contrib import admin
from 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.twitter.urls', namespace="twitter")),
    url(r'^login/', include('apps.login.urls', namespace="login")),

]
