from django.contrib import admin
from django.conf.urls import url

from blog.views import  IndexView, CategoryView, TagView, PostDetailView
from config.views import links

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(), name='post-detail'),
    url(r'^tag/(?P<tag_id>\d+)$',TagView.as_view(), name='tag-list'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^link/$', links, name='links'),
    url(r'^admin/', admin.site.urls, name='admin'),

]
