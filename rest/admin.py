from django.contrib import admin
from . import models
from .models import Movia, Video


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class MoviaAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
admin.site.register(Movia,MoviaAdmin)
# Register your models here.
