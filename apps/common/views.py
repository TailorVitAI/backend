from functools import wraps

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class Authentication:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class APIException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def handle(view_method):  # type: ignore
        @wraps(view_method)  # type: ignore
        def wrapper(viewset_instance, request, *args, **kwargs):
            try:
                return view_method(viewset_instance, request, *args, **kwargs)  # type: ignore

            except APIException as ex:
                return Response({"error": ex.message}, status=ex.status_code)

            except Exception as ex:
                return Response(
                    {"error": "Unhandled internal server error", "details": str(ex)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return wrapper
