
from django.urls import path, include

from stations.views import bus_stations

urlpatterns = [
    path('', include('stations.urls')),
]