#!/usr/bin/python

import requests


while True:

    fruit = input("Which fruit's nutrition values are you interested in? Write a fruit name: \n")

    response = requests.get("https://www.fruityvice.com/api/fruit/" + fruit.lower(), verify=False)

    print(response.text)
    print("\n")


    print(response.json())
    print("\n")


    response = response.json()
    print("Nutrition values for " + fruit + ":")
    print("carbohydrates: " + str(response["nutritions"]["carbohydrates"]))
    print("protein: " + str(response["nutritions"]["protein"]))
    print("fat: " + str(response["nutritions"]["fat"]))
    print("calories: " + str(response["nutritions"]["calories"]))
    print("sugar: " + str(response["nutritions"]["sugar"]))


    if input("Do you want to check another fruit? Y/N: ").lower() not in {"y", "yes"}:
        break