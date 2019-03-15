from django.contrib import admin
from .models import Education, Skill, Job, Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'other_skills',
        'hobbies',
        'about',
        'educations',
        'skills',
        'jobs'
    ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        'period_work',
        'position',
        'name_company'
    ]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = [
        'period_edu',
        'name_institution',
        'faculty',
        'form_study'
    ]
