from django.contrib import admin
from .models import  Appointment
# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Appointment model.
    """
    list_display = ('customer', 'barber', 'appointment_time', 'status')
    list_filter = ('status', 'appointment_time')
    search_fields = ('customer__user__username', 'barber__user__username')