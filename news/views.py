from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializer import NewsSerializer


menu = [
    {'title':'News', 'url_address':'news'},
    {'title':'About', 'url_address':'about'},
    # {'title':'About us', 'url_address':'about'},
    # {'title':'Settings', 'url_address':'settings'}
]
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

def about(request):
    context = {
        'title':'Список новостей', 
        'news':News.objects.all(),
        'menu':menu
        }
    return render(request, 'news/about.html', context)

def newsID(request, news_id):
    return HttpResponse(f"News = {news_id}")