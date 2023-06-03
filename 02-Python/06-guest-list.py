#!/usr/bin/python

guest_list = ["Angela", "Jack", "Pam", "James", "Lara", "Jason"]

guest_name = input("What is your name?\n")

if guest_name in guest_list:
    print("Welcome!")
else:
    print("You are not invited!")
