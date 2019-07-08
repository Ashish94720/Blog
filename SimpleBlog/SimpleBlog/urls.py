
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
# app_name="posts"
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^posts/',include(('posts.urls','posts'))),
]


if settings.DEBUG:
	urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)