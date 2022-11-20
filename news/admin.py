from django.contrib import admin

from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'photo', 'id_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content',)
    list_editable = ('id_published',)
    list_filter = ('created_at', 'category')
    prepopulated_fields = {"slug":("title", )}

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_superuser', 'gender', 'birth_date')
    list_display_links = ('id', 'username')
    search_fields = ('username',)
    list_editable = ('gender',)
    list_filter = ('gender', 'is_superuser')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Categories)
