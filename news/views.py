from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializer import NewsSerializer

menu = ['Main', 'News', 'About us', 'Settings']
class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Create your views here.
def index(request):

    #News.objects.create(title='News 1', content='Content 1')
    context = {
        'title':'Список новостей', 
        'news':News.objects.all(),
        'menu':menu
        }
    return render(request, 'news/index.html', context)