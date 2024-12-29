from django.db import models
from django.contrib.auth.models import User

class ChargingStation(models.Model):
    # Define choices for charger type
    CHARGER_TYPE_CHOICES = [
        ('TYPE2', 'Type 2'),
        ('CCS', 'CCS'),
        ('CHADEMO', 'CHAdeMO'),
        ('TESLA', 'Tesla Supercharger'),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=100)
    charger_type = models.CharField(
        max_length=50, 
        choices=CHARGER_TYPE_CHOICES,
        default='TYPE2'  # Default option
    )
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.user} at {self.station}"
