from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import (RegisterSerializer, UserSerializer, ChangePasswordSerializer,
                          BarberSerializer, CustomerSerializer)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CustomerListView(generics.ListAPIView):
    """
    get:
    Return list of all users with user_type 'customer'.
    """
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.filter(profile__user_type='customer')

class BarberListView(generics.ListAPIView):
    """
    get:
    Return a list of all users with user_type 'barber'.
    """
    serializer_class = BarberSerializer
    permission_classes = [permissions.AllowAny]  # or IsAuthenticated if you want to restrict

    def get_queryset(self):
        return User.objects.filter(profile__user_type='barber')

class RegisterView(generics.CreateAPIView):
    """
    post:
    Register a new user.

    Required fields: `username`, `email`, `password`, `password2`.

    Returns the created user object on success.

    Example request body:
    {
        "username": "amir",
        "email": "amir@example.com",
        "password": "StrongPassword123",
        "password2": "StrongPassword123"
    }
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="Register a new user",
        request_body=RegisterSerializer,
        responses={201: UserSerializer, 400: "Bad Request"}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    get:
    Retrieve the currently authenticated user's profile.

    put:
    Update the authenticated user's profile fields (`username`, `email`).

    Requires authentication via JWT.

    Example request header:
    Authorization: Bearer <access_token>

    Example response:
    {
        "id": 1,
        "username": "amir",
        "email": "amir@example.com"
    }
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    @swagger_auto_schema(
        operation_description="Retrieve user profile",
        responses={200: UserSerializer}
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update user profile",
        request_body=UserSerializer,
        responses={200: UserSerializer, 400: "Bad Request"}
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ChangePasswordView(generics.UpdateAPIView):
    """
    put:
    Change the authenticated user's password.

    Requires fields: `old_password`, `new_password`.

    Validates the old password and enforces Django's password strength rules.

    Example request body:
    {
        "old_password": "OldPass123",
        "new_password": "NewStrongerPass456"
    }

    Returns success message on completion.
    """
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    @swagger_auto_schema(
        operation_description="Change user password",
        request_body=ChangePasswordSerializer,
        responses={200: openapi.Response("Password updated"), 400: "Bad Request"}
    )
    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()
            update_session_auth_hash(request, user)

            return Response({"detail": "Password updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)