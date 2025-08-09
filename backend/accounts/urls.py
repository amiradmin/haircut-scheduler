from django.urls import path
from .views import RegisterView, ProfileView, ChangePasswordView, BarberListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('barbers/', BarberListView.as_view(), name='barber-list'),
]
