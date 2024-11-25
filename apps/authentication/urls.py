from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserView


import apps.authentication.views as VIEWS


router = DefaultRouter()

router.register(
    r"users",
    VIEWS.UsersViewSet,
    basename="users",
)

urlpatterns = [
    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "user/",
        UserView.as_view(),
        name="user",
    ),
    path(
        "",
        include(router.urls),
    ),
]
