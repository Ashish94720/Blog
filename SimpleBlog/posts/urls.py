
from django.conf.urls import url
from django.urls import path, include, re_path

from posts.views import post_create,post_detail,post_list,post_update,post_delete
urlpatterns = [
    re_path(r'^$',post_list,name='list'),
    re_path(r'^create/$',post_create),
    re_path(r'^(?P<slug>[\w-]+)/$',post_detail,name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$',post_update,name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$',post_delete),
]