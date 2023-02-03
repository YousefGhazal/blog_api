from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','slug','published', 'status']
    list_filter = ['status','slug', 'published',]
    
    search_fields = ['title', 'body']
    date_hierarchy = 'published'
    ordering = ['status', 'published']