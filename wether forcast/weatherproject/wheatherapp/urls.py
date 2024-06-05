from django.urls import path
from . import views

urlpatterns = [
    path('weather_forecast/', views.weather_forecast, name='get_weather_data'),
]
