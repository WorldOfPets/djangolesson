from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from rest_framework import generics
from .models import *
from .serializer import NewsSerializer
from .forms import *
from django.views.generic import ListView, CreateView
from django.db.models import Q 

menu = [
    {'title':'News', 'url_address':'news'},
    {'title':'About us', 'url_address':'about'},
    {'title':'Add news', 'url_address':'addnews'},
    # {'title':'Settings', 'url_address':'settings'}
]
class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Create your views here.
class NewsHome(ListView):
    model = News
    template_name = 'news/index.html'
    extra_context = {'title':'Список новостей'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_queryset(self):
        return News.objects.filter(id_published=True)

def index(request):

    #News.objects.create(title='News 1', content='Content 1')
    context = {
        'title':'Список новостей', 
        'menu':menu,
        'cat_selected':None
        }
    return render(request, 'news/index.html', context)

def about(request):
    context = {
        'title':'Список новостей', 
        'menu':menu
        }
    return render(request, 'news/about.html', context)

def newsID(request, news_id):
    post = get_object_or_404(News, slug=news_id)
    
    context = {
        'post':post,
        'menu':menu,
        'title':post.title,
        'cat_selected':post.category.slug
    }
    return render(request, 'news/news_one.html', context)

def category(request, cats_id):
    context = {
        'title':'Список новостей',
        'menu':menu,
        'cat_selected':cats_id
        }
    return render(request, 'news/index.html', context)

class AddNews(CreateView):
    form_class = AddPostForm
    template_name = "news/addnews.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавление статьи"
        context['menu'] = menu
        return context

# def addnews(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('news')
#     else:
#         form = AddPostForm()
#     context = {
#         'title':'Добавить статью',
#         'menu':menu,
#         'form':form
#         }
#     return render(request, 'news/addnews.html', context)