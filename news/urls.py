from django.urls import path
from .views import *
urlpatterns = [
    path('', NewsHome.as_view(), name='news'),
    path('about/', about, name='about'),
    path('news/<slug:news_id>/', newsID, name='newsid'),
    path('category/<slug:cats_id>/', category, name='category'),
    path('addnews/', AddNews.as_view(), name='addnews')
]