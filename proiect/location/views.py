from django.shortcuts import render

from location.models import Location

from location

# Create your views here.
class LocationView(ListView):
    model = Location
    template_name = 'location/location_index.html'
