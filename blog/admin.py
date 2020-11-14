from django.contrib import admin
from .models import Article, Author, Category, Tag

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ['title', 'category', 'author', 'view_count', 'timestamp', 'is_published', 'is_trending', 'is_editors_pick', 'is_featured']
    list_filter = ['category', 'author', 'view_count', 'timestamp', 'is_published', 'is_trending', 'is_editors_pick', 'is_featured']
    list_display_links = ['title']
    list_editable = ['view_count', 'is_published', 'is_trending', 'is_editors_pick', 'is_featured']
    search_fields = ['title', 'body', 'category']
    list_per_page = 25
    readonly_fields = ['timestamp', 'updated']
    slug = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'is_featured']
    list_filter = ['name', 'timestamp', 'is_featured']
    list_display_links = ['name']
    list_editable = ['is_featured']
    search_fields = ['name', 'summary']
    slug = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_joined', 'is_featured']
    list_filter = ['name', 'date_joined', 'is_featured']
    list_display_links = ['name']
    search_fields = ['name', 'summary']
    list_editable = ['is_featured']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)