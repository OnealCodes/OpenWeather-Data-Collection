
# collecting Weather data from openWeather
import requests

# api key
API_KEY = "79b5569d5e44702ed6ba125b2af265d5"

def get_lat_lon(city_name):
    """"Given a location return the latitude and longitude"""
    try:
        geo_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}"
        response = requests.get(url = geo_api).json()
        lat = response[0]['lat']
        long = response[0]['lon']
    except:
        print("Couldnt connect to API.")
    return (long, lat)

    
# get data
def get_weather_data(latitude, longitude):
    """Given a latitude and longitude data return the data"""
    weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
    response = requests.get(url = weather_api).json()

    data = {
    'country': response['sys'] ['country'],
    'city': response['name'],
    'longitude': response['coord']['lon'],
    'latitude': response['coord']['lat'],
    'temp': response['main']['temp'],
    'temp_min': response['main']['temp_min'],
    'temp_max': response['main']['temp_max'],
    'pressure': response['main']['pressure'],
    'humidity': response['main']['humidity'],
    'sea_level': response['main']['sea_level'],
     'ground_level': response['main']['grnd_level'],
    'wind_speed': response['wind']['speed'],
    'wind_degree': response['wind']['deg'],
    'sunrise': response['sys']['sunrise'],
    'sunset': response['sys']['sunset'],
    'description': response['weather'][0]['description']
} 
    return (data)
    
    



# # url
# weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"

# # make a request
# request = requests.get(weather_api).json()

# # data collection



# status
long = get_lat_lon("Abuja")[0]
lat = get_lat_lon("Abuja")[1]


print(get_weather_data(latitude=lat, longitude=long))