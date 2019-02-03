from django.contrib import admin
from .models import AccountHr


@admin.register(AccountHr)
class AccountHrAdmin(admin.ModelAdmin):
    list_display = [
        'type_account', 'id_user'
    ]

