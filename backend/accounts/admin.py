from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserProfile model.
    """
    list_display = ('user', 'user_type', 'phone')
    list_filter = ('user_type',)
    search_fields = ('user__username', 'phone')