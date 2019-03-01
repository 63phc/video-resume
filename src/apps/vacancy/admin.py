from django.contrib import admin

from .models import Vacancy, Tag


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'description', 'slug',
    ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
    prepopulated_fields = {'slug': ('name',)}
