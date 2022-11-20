from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .utils import DataMixins
from .models import *
from .serializer import NewsSerializer
from .forms import *
from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Q 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

menu = [
    {'title':'News', 'url_address':'news'},
    {'title':'About us', 'url_address':'about'},
    {'title':'Add news', 'url_address':'addnews'},
    # {'title':'Settings', 'url_address':'settings'}
]

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    def perform_create(self, serializer):
        print(self.request.user)

    def retrieve(self, request, *args, **kwargs):
        print(request.user.pk)
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        print(request.user)
        return super().list(request, *args, **kwargs)

    
    
    #permission_classes = (IsAdminUser, )
# class NewsApiCreateList(generics.ListCreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
# class NewAPIRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
# class NewsAPIView(generics.ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# Create your views here.
class NewsHome(DataMixins, ListView):
    paginate_by = 3
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Страница новостей")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(id_published=True).select_related('category')

class RegisterUser(DataMixins, CreateView):
    form_class = RegisterUserForm
    template_name = 'news/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('news')

class AuthUser(DataMixins, LoginView):
    form_class = AuthenticationUserForm
    template_name = 'news/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('news')

# class AboutPage(DetailView):
#     template_name = 'news/about.html'

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Список новостей'
#         context['menu'] = menu
@login_required
def about(request):
    context = {
        'title':'Список новостей', 
        'menu':menu
        }
    return render(request, 'news/about.html', context)

class NewsOne(DataMixins, DetailView):
    model = News
    template_name = "news/news_one.html"
    slug_url_kwarg = 'news_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        
        c_def = self.get_user_context(title="Новость " + str(context['post'].title),
            cat_selected=context['post'].category.slug)
        return dict(list(context.items()) + list(c_def.items()))
class CategoryView(DataMixins, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Categories.objects.get(slug=self.kwargs['cats_id'])
        c_def = self.get_user_context(title="Категория - " + 
            str(c.title), cat_selected=c.slug )
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return News.objects.filter(id_published=True, 
            category__slug=self.kwargs['cats_id']).select_related('category')
class AddNews(LoginRequiredMixin, DataMixins, CreateView):
    form_class = AddPostForm
    template_name = "news/addnews.html"
    login_url = reverse_lazy('news')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))

# def register(request):
#     return HttpResponse("Registration")

# def login(request):
#     return HttpResponse("Login")
def logout_user(request):
    logout(request)
    return redirect('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# def index(request):
#     #News.objects.create(title='News 1', content='Content 1')
#     context = {
#         'title':'Список новостей', 
#         'menu':menu,
#         'cat_selected':None
#         }
#     return render(request, 'news/index.html', context)

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

# def category(request, cats_id):
#     context = {
#         'title':'Список новостей',
#         'menu':menu,
#         'cat_selected':cats_id
#         }
#     return render(request, 'news/index.html', context)

# def newsID(request, news_id):
#     post = get_object_or_404(News, slug=news_id)
    
#     context = {
#         'post':post,
#         'menu':menu,
#         'title':post.title,
#         'cat_selected':post.category.slug
#     }
#     return render(request, 'news/news_one.html', context)