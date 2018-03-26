from django.conf.urls import include, url
from django.contrib import admin
import polls
from polls.views import post_list
##from mysite import settings
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # Examples:
     url(r'^$', post_list, name='post_list'),
     url(r'^admin', include(admin.site.urls), name='admin'),
     url(r'^auth/', include('loginsys.urls'), name='loginsys'),
     url(r'^', include('polls.urls'), name='polls'),
     ##url(r'^ckeditor/', include('ckeditor_uploader.urls'))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
