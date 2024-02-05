
# collecting Weather data from openWeather
import requests

# parameters
latitude = 6.6018
longitude = 3.3515
API_KEY = "79b5569d5e44702ed6ba125b2af265d5"

# url
weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"

# make a request
request = requests.get(weather_api).json()

# data collection
data = {
    'country': request['sys'] ['country'],
    'city': request['name'],
    'longitude': request['coord']['lon'],
    'latitude': request['coord']['lat'],
    'temp': request['main']['temp'],
    'temp_min': request['main']['temp_min'],
    'temp_max': request['main']['temp_max'],
    'pressure': request['main']['pressure'],
    'humidity': request['main']['humidity'],
    'sea_level': request['main']['sea_level'],
     'ground_level': request['main']['grnd_level'],
    'wind_speed': request['wind']['speed'],
    'wind_degree': request['wind']['deg'],
    'sunrise': request['sys']['sunrise'],
    'sunset': request['sys']['sunset'],
    'description': request['weather'][0]['description']
}


# status
print(data)