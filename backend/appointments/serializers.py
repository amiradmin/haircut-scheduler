from rest_framework import serializers
from .models import Appointment

from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    # Add this to get customer's username as customer_name
    customer_name = serializers.CharField(source='customer.user.username', read_only=True)
    barber_name = serializers.CharField(source='barber.user.username', read_only=True)

    class Meta:
        model = Appointment
        # Include model fields + your new computed fields
        fields = [
            'id',
            'customer',
            'customer_name',
            'barber',
            'barber_name',
            'appointment_time',
            'status',
        ]

