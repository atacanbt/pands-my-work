# nameAndAge.py
# this program prompts person's name and age and outputs these values with greetings
# author: Atacan Buyuktalas

name = input("Enter your name: ")
age = input("Enter your age: ")

# print(f'Hello {name}, \tyour age is {age}.')

txt = "Hello {0}, \tyour age is {1}"
print(txt.format(name, age))
