from django.contrib import admin
from .models import AccountWorker


@admin.register(AccountWorker)
class AccountWorkerAdmin(admin.ModelAdmin):
    list_display = [
        'id_user',
        'type_account',
        'number_of_resumes'
    ]
