from django.contrib import admin
from . import models
from .models import Cinema, Serial, Video, Multifilm, MultifilmVideo

class CinemaAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre')
    list_filter = ('genre',)
    search_fields = ('title',)

admin.site.register(Cinema, CinemaAdmin)


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class SerialAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

admin.site.register(Serial, SerialAdmin)

class MultifilmVideoInline(admin.TabularInline):
    model = MultifilmVideo
    extra = 1

class MultiAdmin(admin.ModelAdmin):
    inlines = [MultifilmVideoInline]
admin.site.register(Multifilm, MultiAdmin)
