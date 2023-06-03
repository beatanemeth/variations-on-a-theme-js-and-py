#!/usr/bin/python

import random


print("PLAY 'ROCK, PAPER, SCISSOR' WITH ME!\n I made my choice, it is now your turn!\n")

you_wins = 0
computer_wins = 0

items = ["rock", "paper", "scissor"]


while True:

    random_num = random.randint(0, 2)
    #print("Random number: " + str(random_num))

    for item in items:
        if items.index(item) == random_num:
            #print(items.index(item))
            #print(items[random_num])
            computer_choice = items[random_num]


    your_choice = (input("Choose one from 'rock / paper / scissor': ")).lower()


    if computer_choice ==  your_choice:
        print("Even")

    elif computer_choice == "rock" and your_choice == "paper":
        print("You won!")
        you_wins +=1

    elif computer_choice == "paper" and your_choice == "scissor":
        print("You won!")
        you_wins +=1

    elif computer_choice == "scissor" and your_choice == "rock":
        print("You won!")
        you_wins +=1

    else:
        print("You lost!")
        computer_wins += 1


    if input("Continue? Y/N: ").lower() not in {"y", "yes"}:
        break


print("You won", you_wins, "times.")
print("The computer won", computer_wins, "times.")
print("See you next time!")