from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', NewsHome.as_view(), name='news'),
    path('about/', cache_page(60)(about), name='about'),
    path('news/<slug:news_id>/', NewsOne.as_view(), name='newsid'),
    path('category/<slug:cats_id>/', CategoryView.as_view(), name='category'),
    path('addnews/', AddNews.as_view(), name='addnews'),
    path('registration/', RegisterUser.as_view(), name='register'),
    path('login/', AuthUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]