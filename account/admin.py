from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra info', {'fields': ('phone', 'birth_date', 'gender', 'description', 'avatar')}),
    )
