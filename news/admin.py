from django.contrib import admin

from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'photo', 'id_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content',)
    list_editable = ('id_published',)
    list_filter = ('created_at', 'category')
    prepopulated_fields = {"slug":("title", )}

admin.site.register(News, NewsAdmin)
admin.site.register(Categories)
