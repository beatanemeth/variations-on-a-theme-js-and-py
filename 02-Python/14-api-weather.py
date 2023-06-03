#!/usr/bin/python

import requests


while True:

    api_key = "YOUR_OWN_API_KEY_AT_OpenWeatherMap"
    unit = "metric"

    query = input("Write a city name: ")

    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + query + "&appid=" + api_key + "&units=" + unit, verify=False)

    response = response.json()

    temp = response["main"]["temp"]
    description = response["weather"][0]["description"]

    print("The weather is currently " +  description + ".")
    print("\nThe temperature in " + query + " is: " + str(temp) + " degrees Celsius.\n")

    
    if input("Do you want to check another city? Y/N: ").lower() not in {"y", "yes"}:
        break