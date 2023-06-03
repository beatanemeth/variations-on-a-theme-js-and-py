#!/usr/bin/python

count = 5

while count > 0:
    if count == 1:
        bottle = bottleDown = "bottle"
    elif count == 2:
        bottle = "bottles"
        bottleDown = "bottle"
    else:
        bottle = bottleDown = "bottles"
   
    print(f'{count} {bottle} of beer on the wall, {count} {bottle} of beer.\n Take one down and pass it around, {count -1} {bottleDown} of beer on the wall.\n')

    count -= 1