#!/usr/bin/python

your_age = int(input("What is your age? \n"))

def time_left(age):

    time_left = 90 - age

    months = time_left * 12
    weeks = time_left * 52
    days = time_left * 365

    print("\nYou have " + str(days) + " days, or " + str(weeks) + " weeks, or " + str(months) + " months left until age 90.")


time_left(your_age)