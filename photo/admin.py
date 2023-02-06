from django.contrib import admin
from .models import Albom, Photo, AboutMe, Blog
from django.utils.safestring import mark_safe


class AlbomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'picture', 'description', 'prewiew')
    list_display_links = ('id', 'name', 'date')
    search_fields = ('title', 'name')

    def prewiew(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="max-width: 70%;">')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'albom_id', 'prewiew')
    list_display_links = ('id', 'prewiew')
    search_fields = ('albom_id',)

    def prewiew(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="max-width: 10%;">')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')


admin.site.register(Albom, AlbomAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(AboutMe)
admin.site.register(Blog, BlogAdmin)
