# articles/admin.py

from django.contrib import admin

from . import models

class SeansInline(admin.TabularInline): 
    model = models.Seans
    extra = 2

class CinemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    inlines = [
        SeansInline,
    ]

class SeansAdmin(admin.ModelAdmin):
    list_display = ('id', 'seans', 'cinema')

admin.site.register(models.Cinema, CinemaAdmin) 
admin.site.register(models.Seans, SeansAdmin)