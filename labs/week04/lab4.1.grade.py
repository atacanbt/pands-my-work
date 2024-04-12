# grade.py
# this program reads in a students percentage mark and prints out the corresponding grade
# author: Atacan Buyuktas
'''
percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
elif percentage < 70:
    print("Merit 1")
else: # the only option left is between 70 and 100
    print("Distinction")
'''
import math

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
# I can only think this way, I imported the math module and used 'math.ceil' to round a number  up to nearest integer 
elif percentage >= 69.5:
    math.ceil(percentage)
    print("Distinction")
elif percentage < 70:
    print("Merit 1")
else: # the only option left is between 70 and 100
    print("Distinction")
