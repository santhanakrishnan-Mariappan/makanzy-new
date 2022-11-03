from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    AllUnits = Units.objects.all()
    return render(request, "home/home1.html", {"units": AllUnits})


def locationBiased(request, location):
    getAllLocations = Units.objects.filter(location=location)
    return render(request, "home/test.html", {"units": getAllLocations})


def BuildingsBiased(request, buildings):
    getAllBuildings = Units.objects.filter(buildings=buildings)
    return render(request, "home/filtered.html", {"units": getAllBuildings})

def unitTypesBiased(request, unitTypes):
    getAllUnitTypes = Units.objects.filter(unitTypes=unitTypes)
    return render(request, "home/test.html", {"units": getAllUnitTypes})
  # test
def dimensionsBiased(request, dimensions):
    getAllDimensions = Units.objects.filter(dimensions=dimensions)
    return render(request, "home/test.html", {"units": getAllDimensions})

def amenityBiased(request, amenity):
    getAllAmenity = Units.objects.filter(amenity=amenity)
    return render(request, "home/test.html", {"units": getAllAmenity})

def userTypeBiased(request, userType):
    getByUserTypes = Units.objects.filter(userType=userType)
    return render(request, "home/test.html", {"units": getByUserTypes})




