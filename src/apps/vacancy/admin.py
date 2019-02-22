from django.contrib import admin

from .models import Vacancy, Tag


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
