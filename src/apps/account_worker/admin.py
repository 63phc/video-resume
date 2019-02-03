from django.contrib import admin
from .models import AccountWorker


@admin.register(AccountWorker)
class AccountWorkerAdmin(admin.ModelAdmin):
    list_display = [
        'type_account', 'id_user'
    ]
