#!/usr/bin/python

word = input("Enter any word, all in lowercase: \n")

word_first_char = word[0:1]
word_first_char_upper = word_first_char.upper()
word_rest_char = word[1:]

print("\nLook, I can turn your word's first character into uppercase: \n" + word_first_char_upper + word_rest_char)
