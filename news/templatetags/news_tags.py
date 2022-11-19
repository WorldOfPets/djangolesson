from django import template
from news.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return Categories.objects.all()

@register.inclusion_tag('news/list_cats.html')
def show_cats(cat_select=None, sort=None):
    if not sort:
        cats = Categories.objects.all()
    else:
        cats = Categories.objects.order_by(sort)
        
    return {"cats":cats, "cat_selected":cat_select}

@register.inclusion_tag('news/list_news.html')
def show_news(cats=None):
    if not cats:
        news = News.objects.all()
    else:
        cat = Categories.objects.get(slug=cats)
        news = News.objects.filter(category=cat.pk)
    return {'news':news.filter(id_published=True)}

