from django.contrib import admin

from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'slug', 'text']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Answer)
class AnswersAdmin(admin.ModelAdmin):
    list_display = [
        'answer', 'question']
