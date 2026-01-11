from django.contrib import admin
from .models import CustomUser, Profile 
from unfold.admin import ModelAdmin
@admin.register(CustomUser)
# Register your models here.
class CustomUserAdmin(ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('email',)

    fieldsets = (
        ('User information', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        )


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')
    search_fields = ('user__email', 'first_name', 'last_name')
    ordering = ('user__email',)
