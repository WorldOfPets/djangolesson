from django.shortcuts import render

from .models import News

# Create your views here.
def index(request):
    News.objects.create(title='News 1', content='Content 1')
    context = {'title':'Список новостей', 'news':News.objects.all()}
    return render(request, 'news/index.html', context)