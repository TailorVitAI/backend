from drf_spectacular.utils import extend_schema
from rest_framework import views, viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.common.views import Authentication

from .models import User
from .serializers import UserSummarySerializer, UserCreateSerializer

TAGS = ["Authentication"]


class CustomTokenObtainPairView(TokenObtainPairView):

    @extend_schema(tags=TAGS)
    def post(self, request: views.Request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):

    @extend_schema(tags=TAGS)
    def post(self, request: views.Request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class UserView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200: UserSummarySerializer}, tags=TAGS)
    def get(self, request):
        user: User = request.user
        serializer = UserSummarySerializer(user)
        return Response(serializer.data)


class UsersViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.GenericViewSet,
    Authentication,
):
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "first_name",
        "last_name",
        "username",
    ]
    serializer_classes = {
        "list": UserSummarySerializer,
        "create": UserCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, None)

    def get_queryset(self):
        role = self.request.query_params.get("role", None)
        if role:
            queryset = User.objects.filter(
                role=role,
            )
        else:
            queryset = User.objects.all()

        return queryset

    @extend_schema(tags=["Authentication"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=["Authentication"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
