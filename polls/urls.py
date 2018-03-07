from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>\d+)/$', views.post_details, name='post_details'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^page/(\d+)/$', views.listing, name='listing'),
    url(r'^post/addcomment/(?P<pk>\d+)/$', views.new_comment, name='new_comment'),
]