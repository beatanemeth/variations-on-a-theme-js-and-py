#!/usr/bin/python

fibonacci_numbers = []

def fibonacci_generator():
    num_items = int(input("Enter a whole number and get the list of Fibonacci's numbers: "))

    if num_items == 1:
        fibonacci_numbers.append(0)
    
    elif num_items == 2:
        fibonacci_numbers.extend([0, 1])
    
    else:
        fibonacci_numbers.extend([0, 1])

        for _ in range(2, num_items):
            last_item = fibonacci_numbers[len(fibonacci_numbers)-1]
            before_last_item = fibonacci_numbers[len(fibonacci_numbers)-2]
            next_item = last_item + before_last_item
            fibonacci_numbers.append(next_item)

    print(fibonacci_numbers)



fibonacci_generator()