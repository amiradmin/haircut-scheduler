from django.db import models
from accounts.models import UserProfile


class Appointment(models.Model):
    """
    Model representing an appointment between a customer and a barber.
    """
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='appointments')
    barber = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='barber_appointments')
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ])

    def __str__(self):
        return f"{self.customer.user.username} with {self.barber.user.username} on {self.appointment_time}"
