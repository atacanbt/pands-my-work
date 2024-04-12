# messingwithif.py
# program to show the use of if statement

# format of an if statement
# if (condition):
#    statements

# if (condition):
#    statements(if true)
# else:
#    statements(if false)

# if (condition1):
#    statements(if condition1 is true)
# elif (condition2):
#    statements(if condition1 is false but condition2 is true)
# else:
#    statements(if both condition1 and condition2 are false)

# when the if statement is true, indented code is executed
a = 1
if True:
    print("We are in the statement")
    a = 22

print("sanity", a)

# when the if statement is false, indented code is not executed
b = 1
if False:
    print("We are in the statement1")
    b = 22
print("sanity1", b)

c = 3 # singe = assignemnt
if c == 1: # double == comparison/checking
    print("c is one")
else:
    print("c is not one")
# isinstance(d, int) of is a function that checks if the variable is of a certain type
d = 3
if isinstance(d, int) and d == 3:
    print("d is three")
else:
    print("d is not three")

e = 10
if not isinstance(e, int):
    print("Please submit an integer")
elif e < 0:
    print("e is negative")
elif e >= 10:
    print("e is 10 or greater than 10")
else:
    print("e is between 0 and 9 inclusive")