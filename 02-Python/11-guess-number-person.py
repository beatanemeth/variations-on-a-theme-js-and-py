#!/usr/bin/python

#  We are guessing which number the computer is thinking of.

while True:

    import random

    print("I am thinking of a number between 0 and 5.")

    random_number = random.randint(0, 5)

    guess_number = int(input("Take a guess: "))

    guess_count = 1

    if guess_number != random_number:

        while guess_number != random_number:
            guess_number = int(input("Nope! Take a new guess: "))
            guess_count += 1

        else: 
            print("You got it! It was number: " + str(random_number) + "." + " It has taken you " + str(guess_count) + " guesses!")

    else:
        print("You got it from the first attempt!")


    if input("Continue? Y/N: ").lower() not in {"y", "yes"}:
        break