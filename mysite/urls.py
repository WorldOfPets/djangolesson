"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from news.views import *
from mysite import settings
from django.views.static import serve as mediaserve
from django.urls import re_path
from news.views import pageNotFound
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('api/v1/', include(router.urls))
    # path('api/v1/newslist/', NewsApiCreateList.as_view()),
    # path('api/v1/newslist/<int:pk>/', NewAPIRUD.as_view())
] 

if settings.DEBUG:
    urlpatterns += [
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$', 
        mediaserve, {'document_root':settings.MEDIA_ROOT}),
        path('__debug__/', include('debug_toolbar.urls')),
    ]
else:
    urlpatterns += [
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
        mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]

handler404 = pageNotFound
