from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views
from .models import Post, Comments, PostStatistic
from .views import PostLikeAPIToggle


app_name = 'ajax'
urlpatterns = [
    url(r'^$', views.post_list ),
    url(r'^post/(?P<pk>\d+)/lik/$', views.add_like, name='like-add'),
    url(r'^post/(?P<pk>\d+)/$', views.post_details, name='post_details'),
    url(r'^api/(?P<pk>\d+)/like/$', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/addcomment/(?P<pk>\d+)/$', views.new_comment, name='new_comment'),


]
