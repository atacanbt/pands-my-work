# guess2.py
# this program prompts user to guess a pre-defined number, also gives hint whether their guess is too high or low
# author: atacan buyuktalas

number_to_guess = 30

guess = int(input("Please guess a number: "))
while guess != number_to_guess:
    if guess < number_to_guess:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Please guess it again: "))
print("Well done! Yes, the number was", number_to_guess)