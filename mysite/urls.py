from django.conf.urls import include, url
from django.contrib import admin
import polls
from polls.views import post_list
urlpatterns = [
    # Examples:
     url(r'^$', post_list, name='post_list'),
     url(r'^admin', include(admin.site.urls), name='admin'),
     url(r'^auth/', include('loginsys.urls'), name='loginsys'),
     url(r'^', include('polls.urls'), name='polls'),


]
