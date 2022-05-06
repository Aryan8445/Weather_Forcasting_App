import requests
from tkinter import *
from pprint import pprint

# Taking user input for the desired location
location = input("Enter the desired location: ")

root = Tk()
root.title("Weathergo.com - Know Weather Anywhere")
root.geometry("600x600")

# API key for weather forecasting
API_Key = "01351ad31924d80208cb67d9b98a9a5f"

# storing the weather data of the desired location
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="

try:
    final_url = weather_url + API_Key
    weather_data = requests.get(final_url).json()
except Exception as A:
    weather_data = "Error"

w_lable = Label(root, highlightbackground="Red", text= weather_data['main'])
w_lable.pack()


root.mainloop()
 
