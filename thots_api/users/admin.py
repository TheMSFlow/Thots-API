from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    model = User

    # Fields shown in the list view
    list_display = ("id", "email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    # Fields to search
    search_fields = ("email",)
    ordering = ("id",)

    # Fields for the "Edit User" page
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),  # only if your model has these
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # Fields for the "Add User" page
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )
