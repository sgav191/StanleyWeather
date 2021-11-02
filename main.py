import tkinter as tk
from os import system
import requests
from urllib.request import urlopen
import pybase64
from datetime import datetime
import time


system('clear')
print ("Hello and welcome to StanleyWeather!")
time.sleep(1)

##Please enter your Weather API Key.
##If you don't have one, you can get one at https://openweathermap.org/api
weatherapikey = "0f75f503806c3176afdd53608d0cb93"
cityname = input ("What city would you like to view the weather of: ")
weatherurl = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&units=metric&appid={weatherapikey}"
apirequests = requests.get(weatherurl)
weather = (apirequests.json())



status = (weather["weather"][0]["description"])
temperature = (weather["main"]["temp"])
temperature = round(temperature)
feels_like_temp = (weather["main"]["feels_like"])
feels_like_temp = round(feels_like_temp)
sunset = (weather["sys"]["sunset"])
sunset = datetime.fromtimestamp(sunset)
sunrise = (weather["sys"]["sunrise"])
sunrise = datetime.fromtimestamp(sunrise)
min_temp = (weather["main"]["temp_min"])
min_temp = round(min_temp)
max_temp = (weather["main"]["temp_max"])
max_temp = round(max_temp)


system('clear')
print (f"""Weather - {cityname}
Status = {status}
Temperature = {temperature}
Feels Like Temperature = {feels_like_temp}
Min Temperature = {min_temp}
Max Temperature = {max_temp}
Sunrise = {sunrise.time()}
Sunset = {sunset.time()}

"""
)
input ("Press enter when you're ready to quit the app...")

#Outro
print ("Exiting StanleyWeather...")
time.sleep(3)
exit()
