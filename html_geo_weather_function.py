import forecastio
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_weather(city):
	api_key=os.environ['WEATHER_KEY']

	geo_locator = Nominatim()
	location = geo_locator.geocode(city)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast \
	(api_key, latitude, longitude).currently()
	temp = forecast.temperature
	summary = forecast.summary
	return "{0:3.0f}° F and {1}.".format(temp, summary) #city1
