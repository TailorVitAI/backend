from django.urls import path, include
from rest_framework.routers import DefaultRouter

import apps.main.views as VIEWS


router = DefaultRouter()
router.register(
    r"profile",
    VIEWS.ProfileViewSet,
    basename="profile",
)
router.register(
    r"experience",
    VIEWS.ExperienceViewSet,
    basename="experience",
)

urlpatterns = [
    path("", include(router.urls)),
]
