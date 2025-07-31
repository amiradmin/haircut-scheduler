from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Extended user profile to store additional information
    related to a Django User, including user type, phone number, and avatar.
    """

    USER_TYPES = (
        ('customer', 'Customer'),
        ('barber', 'Barber'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the user profile.
        """
        return f"{self.user.username} ({self.user_type})"


@receiver(post_save, sender=User)
def create_user_profile(sender: type[User], instance: User, created: bool, **kwargs) -> None:
    """
    Automatically create a UserProfile when a new User is created.
    """
    if created:
        UserProfile.objects.create(user=instance)
