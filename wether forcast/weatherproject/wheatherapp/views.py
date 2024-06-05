from django.contrib import requests
# from urllib import request
from django.shortcuts import render

def get_weather_data(api_key, city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    return data

def weather_forecast(request):
    if request.method == 'POST':
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        city = request.POST.get('city', '')

        weather_data = get_weather_data(api_key, city)

        if weather_data["cod"] == 200:
            context = {
                'city': city,
                'description': weather_data["weather"][0]["description"],
                'temperature': weather_data["main"]["temp"],
                'humidity': weather_data["main"]["humidity"],
            }
        else:
            context = {'error': 'City not found.'}
    else:
        context = {}

    return render(request, 'index.html', context)