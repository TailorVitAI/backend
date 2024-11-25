from rest_framework.routers import DefaultRouter
from django.urls import path, include

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
        VIEWS.CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        VIEWS.CustomTokenRefreshView.as_view(),
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
