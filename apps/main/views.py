from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

import apps.main.models as MODELS
import apps.main.serializers as SERIALIZERS


class ProfileViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.mixins.ListModelMixin,
):
    TAGS = ["Profile"]

    def get_serializer_class(self):
        classes = {
            "list": SERIALIZERS.ProfileSerializer,
            "create": SERIALIZERS.RequestCreateProfileSerializer,
            "partial_update": SERIALIZERS.RequestCreateProfileSerializer,
        }
        return classes[self.action]

    def get_queryset(self):  # type: ignore
        if self.request.user.is_authenticated:
            return MODELS.Profile.objects.filter(user=self.request.user)
        else:
            return MODELS.Profile.objects.none()

    @extend_schema(
        tags=TAGS,
        responses={200: SERIALIZERS.ProfileSerializer},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=TAGS,
        request=SERIALIZERS.RequestCreateProfileSerializer,
        responses={201: SERIALIZERS.ProfileSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=TAGS,
        request=SERIALIZERS.RequestCreateProfileSerializer,
        responses={200: SERIALIZERS.ProfileSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ExperienceViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.DestroyModelMixin,
):
    TAGS = ["Experience"]

    def get_serializer_class(self):
        classes = {
            "list": SERIALIZERS.ExperienceSerializer,
            "create": SERIALIZERS.RequestCreateExperienceSerializer,
            "partial_update": SERIALIZERS.RequestUpdateExperienceSerializer,
        }
        return classes[self.action]

    def get_queryset(self):  # type: ignore
        if self.request.user.is_authenticated:
            return MODELS.Experience.objects.filter(profile__user=self.request.user)
        else:
            return MODELS.Experience.objects.none()

    @extend_schema(
        tags=TAGS,
        responses={200: SERIALIZERS.ExperienceSerializer},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=TAGS,
        request=SERIALIZERS.RequestCreateExperienceSerializer,
        responses={201: SERIALIZERS.ExperienceSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=TAGS,
        request=SERIALIZERS.RequestUpdateExperienceSerializer,
        responses={200: SERIALIZERS.ProfileSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=TAGS)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TailorViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.ListModelMixin,
):
    TAGS = ["Tailor"]

    def get_serializer_class(self):
        classes = {
            "list": SERIALIZERS.TailorSerializer,
            "create": SERIALIZERS.RequestCreateTailorSerializer,
            "partial_update": SERIALIZERS.RequestUpdateTailorSerializer,
        }
        return classes[self.action]

    def get_queryset(self):  # type: ignore
        if self.request.user.is_authenticated:
            return MODELS.Tailor.objects.filter(profile__user=self.request.user)
        else:
            return MODELS.Tailor.objects.none()

    @extend_schema(
        tags=TAGS,
        request=SERIALIZERS.RequestCreateTailorSerializer,
        responses={201: SERIALIZERS.TailorSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=TAGS,
        request=SERIALIZERS.RequestUpdateTailorSerializer,
        responses={200: SERIALIZERS.TailorSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=TAGS)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CurriculumVitaeViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.ListModelMixin,
):
    TAGS = ["Tailor"]

    def get_serializer_class(self):  # type: ignore
        classes = {
            "list": SERIALIZERS.CurriculumVitaeSerializer,
        }
        return classes[self.action]

    def get_queryset(self):  # type: ignore
        if self.request.user.is_authenticated:
            return MODELS.CurriculumVitae.objects.filter(
                tailor__profile__user=self.request.user
            )
        else:
            return MODELS.Tailor.objects.none()

    @extend_schema(
        tags=TAGS,
        responses={200: SERIALIZERS.CurriculumVitaeSerializer},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
