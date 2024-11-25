from rest_framework import views, viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema

from apps.common.views import Authentication

from .models import User
from .serializers import UserSummarySerializer, UserCreateSerializer


class UserView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: UserSummarySerializer})
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

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
