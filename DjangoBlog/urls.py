from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import url, include

from blog.apis import PostViewSet, CategoryViewSet
from blog.views import  IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from config.views import LinkListView
from comment.views import CommentView
from .autocomplete import CategoryAutocomplete, TagAutocomplete


router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^admin/', admin.site.urls, name='admin'),

    url(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(), name='post-detail'),
    url(r'^tag/(?P<tag_id>\d+)$',TagView.as_view(), name='tag-list'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^link/$', LinkListView.as_view(), name='links'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$',AuthorView.as_view(), name='author'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),

    url(r'^api/', include(router.urls),name="api"),
    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),

    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
