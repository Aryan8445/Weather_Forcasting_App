import requests
from pprint import pprint

# API key for weather forecasting
API_Key = "01351ad31924d80208cb67d9b98a9a5f"

# Taking user input for the desired location
location = input("Enter the location: ")

# storing the weather data of the desired location
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="

# Combining both weather url and the API key to store the final result
final_url = weather_url + API_Key

# using reqests module to get the whether data and store the information accordingly
weather_data = requests.get(final_url).json()

#Printing teh data in a readable format
pprint(weather_data) 
