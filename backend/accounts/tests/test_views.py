from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class AccountTests(APITestCase):

    def test_user_registration(self):
        url = reverse('register')  # You must name the RegisterView in your `urls.py`
        data = {
            "username": "amir",
            "email": "amir@example.com",
            "password": "StrongPassword123",
            "password2": "StrongPassword123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_profile_retrieval(self):
        user = User.objects.create_user(username='amir', email='a@example.com', password='123456')
        self.client.force_authenticate(user)
        url = reverse('profile')  # Make sure to name the ProfileView URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'amir')

    def test_change_password(self):
        user = User.objects.create_user(username='amir', email='a@example.com', password='OldPass123')
        self.client.force_authenticate(user)
        url = reverse('change-password')  # Ensure ChangePasswordView is named
        data = {
            "old_password": "OldPass123",
            "new_password": "NewPass456"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
