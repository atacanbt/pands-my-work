# number_queue.py
# this program generates 10 random number upto 100 and display one by one deducting it from the list after display
# author: atacan

import random
# setting the variables
queue = []
number_of_numbers = 10
range_to = 100
# adding random number into the list (queue) upto a certain amaount of number (number_of_numbers)
for n in range(0, number_of_numbers):
    queue.append(random.randint(0,range_to))
# print the queue with 10 numbers in it
print (f"Queue is {queue}")
# display the current number and remove it from the list and diplay the queue
while len(queue) != 0:
    current_number = queue.pop(0)
    print (f"Current number is {current_number} and the queue is {queue}")
# in the example 'f' is missing, hence, it doesn't recognises the format {}
print ("The queue is now empty")