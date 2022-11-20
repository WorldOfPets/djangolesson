from .models import *
from django.db.models import Count
from django.core.cache import cache
menu = [
    {'title':'News', 'url_address':'news'},
    {'title':'About us', 'url_address':'about'},
    {'title':'Add news', 'url_address':'addnews'},
    # {'title':'Settings', 'url_address':'settings'}
]

class DataMixins():
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Categories.objects.annotate(Count('news'))
            cache.set('cats', cats, 60)

        user_menu = menu.copy()
        
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
            user_menu.pop(1)
            # user_menu = list(filter(lambda i: i['title'] != 'About us', user_menu))
            # user_menu = list(filter(lambda i: i['title'] != 'Add news', user_menu))

        context['menu'] = user_menu


        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = None
        return context