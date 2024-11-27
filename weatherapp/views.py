import requests
from django.shortcuts import render
from django.views.generic import *
import datetime


# Create your views here.
def weather_view(request):
    if request.GET:
        city = request.GET['city']
        api_id = ""
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_id)
    try:
        r = requests.get(url=url, params={"q": city, "appid": api_id, "units": "metric"})
        r.raise_for_status()
        json_res = r.json()
        description = json_res['weather'][0]['description']
        weather_icon = json_res['weather'][0]['icon']
        max_temp = json_res['main']['temp_max']
        min_temp = json_res['main']['temp_min']
        temp = json_res['main']['temp']
        wind = json_res['wind']['speed']
        c = {
            "description": description,
            "weather_icon": weather_icon,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "temp": temp,
            "wind": wind,
            "city": city,
            "day": datetime.date.today()
        }
        return render(request, "index.html", context=c)
    except Exception as e:
        print('city name not found !')
    return render(request, "index.html")
