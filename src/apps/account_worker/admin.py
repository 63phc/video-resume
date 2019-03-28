from django.contrib import admin

from .models import AccountWorker, WorkerAnswered


@admin.register(AccountWorker)
class AccountWorkerAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'type_account', 'number_of_resumes'
    ]

    def number_of_resumes(self, obj):
        return obj.resume.count()


@admin.register(WorkerAnswered)
class WorkerAnsweredAdmin(admin.ModelAdmin):
    list_display = [
        'question', 'answer', 'worker'
    ]
