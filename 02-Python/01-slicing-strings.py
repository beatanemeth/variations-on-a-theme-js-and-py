#!/usr/bin/python
# The line above tells the server where to find python.


my_tweet = input("Compose your tweet (a longer one, more then 100 characters): \n")

my_tweet_length = len(my_tweet)

if my_tweet_length < 140:
    print("\nYou have written " + str(my_tweet_length) + " characters, you have " + str(140 - my_tweet_length) + " characters remaining.\n")
else: 
    print("\nYou have written " + str(my_tweet_length) + " characters, you have exceeded the limit with " + str(abs(140 - my_tweet_length)) + " characters.\n")

my_tweet_sliced = my_tweet[0:100]

print("Your sliced tweet (only 100 characters): \n" + my_tweet_sliced)