from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from users.models import User
from users.serializers import RegisterSerializer


class SetJWTtoCookiesView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            response.set_cookie(
                key='jwt-a',
                value=response.data['access'],
                httponly=True,
                secure=True,
                samesite='Lax'
            )
            response.set_cookie(
                key='jwt-r',
                value=response.data['refresh'],
                httponly=True,
                secure=True,
                samesite='Lax'
            )

        return response


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
