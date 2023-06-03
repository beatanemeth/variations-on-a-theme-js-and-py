#!/usr/bin/python

your_numbers = []

def fizz_buzz ():

    repeat = 5
    for _ in range(repeat):
        your_number = int(input("Write a hole number: "))
        your_numbers.append(your_number)
    

    print("\nYour numbers:\n " +  str(your_numbers))

    num_fizz_buzz = []
    for num in range(0, len(your_numbers)):
        fizz_buzz = ""
        if(your_numbers[num] % 3 == 0):
            fizz_buzz += "Fizz"
        if(your_numbers[num] % 5 == 0):
            fizz_buzz += "Buzz"
        if fizz_buzz == "":
            fizz_buzz = your_numbers[num]

        num_fizz_buzz.append(fizz_buzz)
    
    print("\nNumbers replaced with Fizz/Buzz: \n" + str(num_fizz_buzz))


fizz_buzz()
