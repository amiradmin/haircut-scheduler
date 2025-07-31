from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated

class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of all appointments or create a new appointment.

    GET:
        Returns a list of all existing Appointment objects.

    POST:
        Creates a new Appointment instance with the provided data.
    """
    permission_classes = [IsAuthenticated]

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific appointment by ID.

    GET:
        Retrieve details of an Appointment instance.

    PUT:
        Update an Appointment instance entirely.

    PATCH:
        Partially update fields of an Appointment instance.

    DELETE:
        Delete an Appointment instance.
    """
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
