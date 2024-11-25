from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from apps.authentication.urls import urlpatterns as auth_urlpatterns
from apps.main.urls import urlpatterns as main_urlpatterns
from .swagger.urls import urlpatterns as swagger_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include(auth_urlpatterns)),
    path("api/main/", include(main_urlpatterns)),
]

if settings.SWAGGER:
    urlpatterns.append(path("", include(swagger_router)))
