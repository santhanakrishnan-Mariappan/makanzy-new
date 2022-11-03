from django.urls import path, include

from . import views

# app_name = "rentnow"

urlpatterns = [
  path('', views.home, name="home"),
  path('unitTypes/<str:unitTypes>/', views.unitTypesBiased, name="getUnitTypes"),
  path('locations/<str:location>/', views.locationBiased, name="getLocations"),
  path('buildings/<str:buildings>/', views.BuildingsBiased, name="getBuildings"),
  path('dimensions/<str:dimensions>/', views.dimensionsBiased, name="getDimensions"),
  path('amenity/<str:amenity>/', views.amenityBiased, name="getAmenity"),
  path('userType/<str:userType>/', views.userTypeBiased, name="getUserType"),
  # path('userType/<str:userType>/', views.userTypeBiased, name="getUserType"),
]
