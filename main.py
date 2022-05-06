import requests
from tkinter import *
from pprint import pprint

# Taking user input for the desired location
location = input("Enter the desired location: ")

# Basic GUI implementation
root = Tk()
root.title("Weathergo.com - Know Weather Anywhere")
root.geometry("200x100")

# API key for weather forecasting
API_Key = "01351ad31924d80208cb67d9b98a9a5f"

# storing the weather data of the desired location
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="

# storing the values of the desired data 
try:
    final_url = weather_url + API_Key
    weather_data = requests.get(final_url).json()
    country = weather_data['sys']['country']
    city = weather_data['name']
    temp = (weather_data['main']['temp'] - 273.15)
    # Restricting the value to only two ndecimal numbers 
    temp_c = "{:.2f}".format(temp)
    min_temp = weather_data['main']['temp_min']
    clouds = weather_data['clouds']
    
except Exception as A:
    weather_data = "Error"


w_lable = Label(root, text= f''' Country = {country}\n City = {city}\n Temperature = {str(temp_c)}°C\n Clouds = {str(clouds)}''')
w_lable.pack()

root.mainloop()
 
 
