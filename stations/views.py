from rest_framework import viewsets
from .models import ChargingStation, Booking
from .serializers import ChargingStationSerializer, BookingSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Bijuli Sathi App!</h1>")


class ChargingStationViewSet(viewsets.ModelViewSet):
    queryset = ChargingStation.objects.all()
    serializer_class = ChargingStationSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
