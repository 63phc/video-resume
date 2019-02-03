from django.contrib import admin
from django.contrib.auth import get_user_model
from.models import Profile

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'second_name',
        'birth', 'city',
        'family_status', 'phone'
    ]
