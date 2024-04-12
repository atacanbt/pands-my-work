# guess1.py
# this program prompts user to guess a pre-defined number
# author: atacan buyuktalas

number_to_guess = 30

guess = int(input("Please guess a number: "))
while guess != number_to_guess:
    print("Wrong guess!")
    guess = int(input("Please guess it again: "))
print("Well done! Yes, the number was", number_to_guess)