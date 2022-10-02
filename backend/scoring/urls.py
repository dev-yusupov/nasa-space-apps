from django.urls import path
from .views import scoring, about, main, weather, developers

urlpatterns = [
    path("", main, name="main"),
    path("about/", about, name="about"),
    path("scoring/", scoring, name="scoring"),
    path("weather/", weather, name="weather"),
    path("developers/", developers, name="developers")
]