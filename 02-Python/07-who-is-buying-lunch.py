#!/usr/bin/python

import random;

your_input = input("Enter names separated by space: \n")

names = your_input.split()

def whos_paying(names):
    random_num = random.randint(0, len(names)-1)

    random_name = names[random_num]

    print(random_name + " is going to buy lunch today!")


whos_paying(names)