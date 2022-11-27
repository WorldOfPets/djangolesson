from django.urls import path, include, re_path
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r"news", NewsApi)
router.register(r"categ", NewsCategoryApi)

urlpatterns = [
    path('api/', include(router.urls)),
    #path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]