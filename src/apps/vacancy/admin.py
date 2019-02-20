from django.contrib import admin

from src.apps.vacancy.models import Vacancy, Tag


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'description'
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
