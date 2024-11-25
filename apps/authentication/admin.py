from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "role",
        "type",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "base_currency",
        "phone",
        "tax_invoices",
    )
    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "Custom fields",
            {
                "fields": (
                    "role",
                    "type",
                    "base_currency",
                    "identification",
                    "trade_id",
                    "phone",
                    "tax_invoices",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
