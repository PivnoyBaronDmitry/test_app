from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'is_updated', 'is_published')
    list_display_links = ('id', 'title')
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Pizza)
admin.site.register(Topping)