#!/usr/bin/python

#  The computer is guessing which number we are thinking of.

import random

while True:

    my_number = input("I am thinking of a number between 0 and 5. It is number: ")
    
    got_it = False

    number_of_guesses = 1

    while got_it == False:
        
        random_guess_number = random.randint(0, 5)
        print(f'Computer guess: {random_guess_number}')
        
        if random_guess_number == int(my_number):

            got_it = True

            print("Got it! It was a " + str(my_number) + ". It has taken me " + str(number_of_guesses) + " guesses.")

        else:

            number_of_guesses += 1

    if input("Continue? Y/N: ").lower() not in {"y", "yes"}:
        break