# Extra.py
# this program ganarates a random number between 0-100 and prompts user to guess it
# author: atacan

import random

number_to_guess = random.randrange(0,101)
# I used random module to generate a number between the given range

user_guess = int(input("Guess a number: "))

while user_guess != number_to_guess:
# here, I used if-else command to give a hint to the user about their guess
    if user_guess < number_to_guess:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    user_guess = int(input("Please guess it again: "))

print("Well done! The number was", number_to_guess)