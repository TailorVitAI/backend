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
router.register(
    r"tailor",
    VIEWS.TailorViewSet,
    basename="tailor",
)
router.register(
    r"curriculum_vitae",
    VIEWS.CurriculumVitaeViewSet,
    basename="curriculum_vitae",
)

urlpatterns = [
    path("", include(router.urls)),
]
