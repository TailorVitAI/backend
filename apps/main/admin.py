from django.contrib import admin

from apps.common.utils import truncate
import apps.main.models as MODELS


@admin.register(MODELS.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "model_modified_at",
        "model_created_at",
    )
    readonly_fields = (
        "model_modified_at",
        "model_created_at",
    )


@admin.register(MODELS.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "profile",
        "role",
    )
    readonly_fields = (
        "model_modified_at",
        "model_created_at",
    )


@admin.register(MODELS.Tailor)
class TailorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title_truncated",
    )
    readonly_fields = (
        "model_modified_at",
        "model_created_at",
    )

    def title_truncated(self, obj: MODELS.Tailor) -> str:
        return truncate(obj.title)


@admin.register(MODELS.CurriculumVitae)
class CurriculumVitaeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tailor",
        "model_created_at",
    )
    readonly_fields = (
        "model_modified_at",
        "model_created_at",
    )
