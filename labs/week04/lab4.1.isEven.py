# isEven.py
# program to check if a number is even or odd
# author: Atacan Buyuktas

number = int(input("Enter a number: "))
# if the number is divisible by 2, it is even
if (number % 2 == 0):
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")
    