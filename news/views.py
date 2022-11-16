from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializer import NewsSerializer

class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Create your views here.
def index(request):
    News.objects.create(title='News 1', content='Content 1')
    context = {'title':'Список новостей', 'news':News.objects.all()}
    return render(request, 'news/index.html', context)