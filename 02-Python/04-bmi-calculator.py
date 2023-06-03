#!/usr/bin/python

your_weight = int(input("What is your weight? (e.g.: 65) \n"))
your_height = float(input("\nWhat is your height? (e.g.: 1.8) \n"))

def bmi_calculator (weight, height):

    bmi = round((weight /  height**2), 1)

    your_bmi = "Your BMI is "
    so_you = ", so you "

    if bmi < 18.5:
        print(your_bmi + str(bmi) + so_you + "are underweight.") 
    
    if (bmi > 18.5 and bmi < 24.9):
        print(your_bmi + str(bmi) + so_you + "have a normal weight.")

    if bmi > 24.9:
        print(your_bmi + str(bmi) + so_you + "are overweight.")


bmi_calculator(your_weight, your_height)
