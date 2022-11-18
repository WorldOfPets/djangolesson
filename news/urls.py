from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='news'),
    path('about/', about, name='about'),
    path('news/<int:news_id>/', newsID, name='newsid'),
]