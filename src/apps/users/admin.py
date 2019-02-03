from django.contrib import admin
from django.contrib.auth import get_user_model
from.models import Profile

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)

admin.site.register(Profile, UserAdmin)
