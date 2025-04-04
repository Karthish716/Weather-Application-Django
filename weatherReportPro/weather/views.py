from django.shortcuts import render
import requests

def index(request):
    url= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7bd8a87e55ba8c4c9153e3380b335b97'
    city = 'London'

    r=requests.get(url.format(city)).json()


    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    context = {'city_weather': city_weather}
    return render(request,'weather.html', context)
