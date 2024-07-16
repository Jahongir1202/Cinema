from django.contrib import admin
from .models import Cinema
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre')
    list_filter = ('genre',)
    search_fields = ('title',)
admin.site.register(Cinema,CinemaAdmin)
# Register your models here.
