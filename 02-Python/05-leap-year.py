#!/usr/bin/python

while True:

    your_year = int(input("Enter a year and check whether it is a leap year or not!\n"))

    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("\n" + str(year) + " is a leap year\n")
                else:
                    print("\n" + str(year) + " is not a leap year\n")
            else:
                print("\n" + str(year) + " is a leap year\n")
        else:
            print("\n" + str(year) + " is not a leap year\n")

   
    is_leap_year(your_year)


    if input("Do you want to check another year? Y/N: ").lower() not in {"y", "yes"}:
        break