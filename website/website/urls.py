
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    ## Whenever The User requests any music go to
    url(r'^music', include('music.url'))
]
