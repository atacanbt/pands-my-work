# messingwithwhile.py
# messing with while loop during the lecture. 
# author: atacan

# while 'conditions':
#       statements

# two types: Counter Controlled & Sentinal Controlled

# counter controlled: used for loops for counter controlled loops
# sentinal controlled:  if we are reading in from a user, one pattern is
#                       read in from the user, check the while, and then read it again in the body of the while loop
#                   !!! be careful of the infinite loops
#                   make sure to modify what we are checking

# Counter Conrtolled example

count = 0
while count < 10:
    print("count is less", count)
    count += 1
print("at the end the count is ", count)

count = 10
while count >= 0:
    print("countdown", count)
    count -= 1
print("blast off")

# Sentinal Controlled example

val = input("type something (q to quit): ")
while val != 'q':
    print('Hi Mom!')
    val = input("q to quit: ")
print("All done!")