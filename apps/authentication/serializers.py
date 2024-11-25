from rest_framework import serializers

from .models import User
from apps.main.models import Currency


class UserSummarySerializer(serializers.ModelSerializer):
    role_display = serializers.CharField(source="get_role_display")
    base_currency = serializers.CharField(source="base_currency.symbol")

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "base_currency",
            "role",
            "role_display",
            "full_name",
            "is_staff",
        )


class UserCreateSerializer(serializers.ModelSerializer):
    base_currency = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "base_currency",
            "role",
        )

    def validate_base_currency(self, value):
        currency = Currency.objects.get(short_name=value)
        return currency

    def create(self, validated_data: dict):
        user = User.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            base_currency=validated_data["base_currency"],
            role=validated_data["role"],
        )
        return user
