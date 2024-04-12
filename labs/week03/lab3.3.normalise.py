# normalise.py
# this program prompts a string and strips any leading or trailing spaces
# it also converts all letters to lower case
# than it outputs the length of raw string and normalised ones

# author: atacan buyuktalas

raw_string = input('Enter a string: ')
normalised_string = raw_string.strip().lower()

length_of_rawstring = len(raw_string)
length_of_normalised_string = len(normalised_string)

print(f'That string normalised is: {normalised_string}')
print(f'We reduced the input string from {length_of_rawstring} to {length_of_normalised_string} characters.')
