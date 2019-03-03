from django.contrib import admin

from .models import AccountWorker


@admin.register(AccountWorker)
class AccountWorkerAdmin(admin.ModelAdmin):
    list_display = [
        'worker', 'type_account', 'number_of_resumes'
    ]

    def number_of_resumes(self, obj):
        return obj.resume.count()
