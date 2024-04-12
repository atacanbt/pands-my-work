# whileloop.py
# this program promts user for a number until they input '-1'
# author: Atacan Buyuktalas

number = input("Enter a number: ")

# I tried to also cover for any possible empty or string input and came up with below snippet
# it works well if you first try empty input or string then an integer 
# but it gives below error if the first input is integer and the second one is string
# however, I couldn't figure out the problem with my current knowledge 
# the error: 
# Enter a number: 45
# Enter a number: asd
# Traceback (most recent call last):
#   File "/Users/.../pands-weekly-tasks/week04/lab4.1.whileloop.py", line 26, in <module>
#     number = int(input("Enter a number: "))
# ValueError: invalid literal for int() with base 10: 'asd'

if number == "" or not int(number):
    print("You did not enter a number.")
    number = int(input("Enter a number: "))

# I wrote the code with "!=" as we only want them to input '-1'
# then I kept prompting the number with 'while' loop command until they input '-1'
while number != -1:
    number = int(input("Enter a number: "))
print(f"Thank you! {number} is what I was looking for")
