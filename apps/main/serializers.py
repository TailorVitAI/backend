from rest_framework import serializers

import apps.main.models as MODELS


class RequestCreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MODELS.Profile
        exclude = (
            "id",
            "user",
            "model_modified_at",
            "model_created_at",
        )

    def create(self, validated_data):
        request = self.context.get("request")
        profile = MODELS.Profile.objects.create(
            user=request.user,
            **validated_data,
        )
        return profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MODELS.Profile
        exclude = ("user",)


class RequestCreateExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MODELS.Experience
        exclude = (
            "id",
            "profile",
            "model_modified_at",
            "model_created_at",
        )

    def create(self, validated_data):
        request = self.context.get("request")
        profile = MODELS.Profile.objects.get(
            user=request.user,
        )  # TODO: fix for multiple profiles for a single user
        profile = MODELS.Experience.objects.create(
            profile=profile,
            **validated_data,
        )
        return profile


class RequestUpdateExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MODELS.Experience
        exclude = (
            "model_modified_at",
            "model_created_at",
        )


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MODELS.Experience
        fields = "__all__"
