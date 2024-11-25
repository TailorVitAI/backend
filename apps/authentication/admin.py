from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_staff",
    )
    # fieldsets = BaseUserAdmin.fieldsets + (
    #     (
    #         "Custom fields",
    #         {
    #             "fields": (

    #             ),
    #         },
    #     ),
    # )


admin.site.register(User, UserAdmin)
