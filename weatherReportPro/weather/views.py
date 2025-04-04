from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
def index(request):
    url= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7bd8a87e55ba8c4c9153e3380b335b97'

    if request.method == 'POST':
       pass


    form = CityForm()

    # city = 'London'

    cities = City.objects.all()

    weather_data = []

    for city in cities:

      r=requests.get(url.format(city)).json()


      city_weather = {
        'city': city.name,
        'temperature': r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
      }

      weather_data.append(city_weather)

    print(weather_data)  
    context = {'weather_data': weather_data, 'form': form}
    return render(request,'weather.html', context)
